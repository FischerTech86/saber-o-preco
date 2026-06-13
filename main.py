from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def buscar_mercado_livre(produto):
    # Entra no Mercado Livre e busca o produto
    url = f"https://lista.mercadolivre.com.br/{produto}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    resposta = requests.get(url, headers=headers)
    
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        # Procura o primeiro preço que aparece na página
        preco_inteiro = soup.find('span', class_='andes-money-amount__fraction')
        if preco_inteiro:
            return f"R$ {preco_inteiro.text}"
    return "Preço não encontrado"

@app.route('/', methods=['GET', 'POST'])
def index():
    preco = None
    produto = None
    if request.method == 'POST':
        produto = request.form.get('produto')
        if produto:
            preco = buscar_mercado_livre(produto)
            
    return render_template('index.html', preco=preco, produto=produto)

if __name__ == '__main__':
    app.run(debug=True)    servidor_final.serve_forever()
