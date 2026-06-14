from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    lojas = []
    termo = None
    if request.method == "POST":
        termo = request.form.get("produto")
        if termo:
            t = termo.replace(" ", "%20")
            lojas = [
                {"nome": "Mercado Livre", "link": f"https://lista.mercadolivre.com.br/{t}"},
                {"nome": "Amazon", "link": f"https://www.amazon.com.br/s?k={t}"},
                {"nome": "Americanas", "link": f"https://www.americanas.com.br/busca/{t}"},
                {"nome": "Carrefour", "link": f"https://www.carrefour.com.br/busca/?q={t}"},
                {"nome": "Magalu", "link": f"https://www.magazineluiza.com.br/busca/{t}/"},
                {"nome": "Shopee", "link": f"https://shopee.com.br/search?keyword={t}"},
                {"nome": "Kabum", "link": f"https://www.kabum.com.br/busca/{t}"},
                {"nome": "Casas Bahia", "link": f"https://www.casasbahia.com.br/busca/?q={t}"},
                {"nome": "Extra", "link": "https://www.clubeextra.com.br/"},
                {"nome": "Assai", "link": "https://www.assai.com.br/"},
                {"nome": "Tenda Atacadista", "link": "https://www.tendaatacado.com.br/"},
                {"nome": "Oxxo", "link": "https://www.mercadooxxo.com.br/"},
                {"nome": "Coop", "link": "https://www.portalcoop.com.br/"},
                {"nome": "Swift", "link": "https://www.swift.com.br/"}
            ]
    return render_template("index.html", lojas=lojas, termo=termo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
