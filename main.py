from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def buscar_ordenado(produto):
    # Aumentamos o limite para garantir que venham resultados suficientes para ordenar
    url = f"https://api.mercadolivre.com/sites/MLB/search?q={produto}&limit=15"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Filtra apenas itens que possuem preço definido
            lista = [
                {'titulo': item.get('title'), 'preco': item.get('price'), 'link': item.get('permalink')}
                for item in data.get('results', []) if item.get('price') is not None
            ]
            # Ordena do mais barato para o mais caro
            lista.sort(key=lambda x: x['preco'])
            return lista
    except Exception as e:
        print(f"Erro: {e}")
    return []

@app.route("/", methods=["GET", "POST"])
def index():
    produtos = []
    termo = None
    if request.method == "POST":
        termo = request.form.get("produto")
        if termo:
            produtos = buscar_ordenado(termo)
    return render_template("index.html", produtos=produtos, termo=termo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
