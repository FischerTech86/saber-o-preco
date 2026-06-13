from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def buscar_produtos(termo):
    # API oficial para busca no ML Brasil
    url = f"https://api.mercadolivre.com/sites/MLB/search?q={termo}&limit=10"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            produtos = []
            
            for item in data.get('results', []):
                # Extrai os dados garantindo que existem
                preco = item.get('price')
                titulo = item.get('title')
                link = item.get('permalink')
                
                if preco is not None:
                    produtos.append({'titulo': titulo, 'preco': preco, 'link': link})
            
            # Ordena do menor para o maior preço
            return sorted(produtos, key=lambda x: x['preco'])
        else:
            return []
    except Exception:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    produtos = []
    termo = None
    if request.method == "POST":
        termo = request.form.get("produto")
        if termo:
            produtos = buscar_produtos(termo)
    return render_template("index.html", produtos=produtos, termo=termo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
