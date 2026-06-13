from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    produto = None
    link = None
    if request.method == "POST":
        produto = request.form.get("produto")
        if produto:
            # Cria o link de busca direta do Mercado Livre
            termo = produto.replace(" ", "%20")
            link = f"https://lista.mercadolivre.com.br/{termo}"
    return render_template("index.html", produto=produto, link=link)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
