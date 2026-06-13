from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def buscar_na_api_ml(produto):
    # API oficial do Mercado Livre
    url = f"https://api.mercadolivre.com/sites/MLB/search?q={produto}&limit=3"
    try:
        response = requests.get(url)
        data = response.json()
        resultados = []
        
        # Pega os 3 primeiros resultados da API
        for item in data.get('results', []):
            titulo = item.get('title')
            preco = item.get('price')
            link = item.get('permalink')
            resultados.append({'titulo': titulo, 'preco': preco, 'link': link})
        return resultados
    except:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    produtos_encontrados = []
    termo_busca = None
    if request.method == "POST":
        termo_busca = request.form.get("produto")
        if termo_busca:
            produtos_encontrados = buscar_na_api_ml(termo_busca)
    return render_template("index.html", produtos=produtos_encontrados, termo=termo_busca)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
