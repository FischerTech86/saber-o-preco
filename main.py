from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def buscar_mercado_livre(produto):
    termo_busca = produto.replace(" ", "%20")
    url = f"https://lista.mercadolivre.com.br/{termo_busca}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    
    try:
        resposta = requests.get(url, headers=headers)
        soup = BeautifulSoup(resposta.text, "html.parser")
        
        # Procurar pelo contêiner do produto
        item = soup.find("div", class_="ui-search-result__wrapper")
        
        if item:
            # Captura o link
            link_tag = item.find("a", class_="ui-search-link")
            link = link_tag["href"] if link_tag else "#"
            
            # Tenta pegar o preço de classes diferentes que o ML usa
            preco_tag = item.find("span", class_="andes-money-amount__fraction")
            if not preco_tag:
                preco_tag = item.find("span", class_="andes-money-amount ui-search-price__part")
            
            preco = preco_tag.text if preco_tag else "Não identificado"
            return f"R$ {preco}", link
            
        return "Preço não encontrado", "#"
    except Exception as e:
        return f"Erro na busca: {str(e)}", "#"

@app.route("/", methods=["GET", "POST"])
def index():
    produto = None
    preco = None
    link = "#"
    if request.method == "POST":
        produto = request.form.get("produto")
        if produto:
            preco, link = buscar_mercado_livre(produto)
    return render_template("index.html", produto=produto, preco=preco, link=link)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
