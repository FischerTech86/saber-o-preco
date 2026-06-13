from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def buscar_mercado_livre(produto):
    termo = produto.replace(" ", "%20")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    url = f"https://lista.mercadolivre.com.br/{termo}"
    
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        item = soup.find("div", class_="ui-search-result__wrapper")
        
        if item:
            preco = item.find("span", class_="andes-money-amount__fraction")
            preco_texto = preco.text if preco else "Consulte o link"
            link = item.find("a", class_="ui-search-link")["href"]
            return f"R$ {preco_texto}", link
        return "Não encontrado", "#"
    except:
        return "Erro na busca", "#"

@app.route("/", methods=["GET", "POST"])
def index():
    produto, preco, link = None, None, "#"
    if request.method == "POST":
        produto = request.form.get("produto")
        if produto:
            preco, link = buscar_mercado_livre(produto)
    return render_template("index.html", produto=produto, preco=preco, link=link)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
