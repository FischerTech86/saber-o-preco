from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def buscar_mercado_livre(produto):
    termo_busca = produto.replace(" ", "-")
    url = f"https://lista.mercadolivre.com.br/{termo_busca}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        resposta = requests.get(url, headers=headers)
        soup = BeautifulSoup(resposta.text, "html.parser")
        item = soup.find("div", class_="ui-search-result__wrapper")
        if item:
            link = item.find("a", class_="ui-search-link")["href"]
            preco_inteiro = item.find("span", class_="andes-money-amount__fraction").text
            return f"R$ {preco_inteiro}", link
        return "Preço não encontrado", "#"
    except:
        return "Erro na busca", "#"

@app.route("/", methods=["GET", "POST"])
def index():
    produto = None
    preco = None
    link = "#"
    if request.method == "POST":
        produto = request.form.get("produto")
        preco, link = buscar_mercado_livre(produto)
    return render_template("index.html", produto=produto, preco=preco, link=link)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
