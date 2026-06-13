from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def buscar_em_lojas(produto):
    termo = produto.replace(" ", "%20")
    resultados = []
    
    # User-Agent moderno para evitar bloqueios
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    url_ml = f"https://lista.mercadolivre.com.br/{termo}"
    
    try:
        res = requests.get(url_ml, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # Procuramos o container principal dos produtos
        item = soup.find("div", class_="ui-search-result__wrapper")
        
        if item:
            # Buscamos o preço de forma mais abrangente
            preco_tag = item.find("span", class_="andes-money-amount__fraction")
            preco_texto = preco_tag.text if preco_tag else "Consulte o link"
            
            link_tag = item.find("a", class_="ui-search-link")
            link = link_tag["href"] if link_tag else url_ml
            
            resultados.append({"loja": "Mercado Livre", "preco": f"R$ {preco_texto}", "link": link})
    except Exception as e:
        print(f"Erro na busca: {e}")
        
    return resultados

@app.route("/", methods=["GET", "POST"])
def index():
    lojas = []
    if request.method == "POST":
        produto = request.form.get("produto")
        if produto:
            lojas = buscar_em_lojas(produto)
    return render_template("index.html", lojas=lojas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
