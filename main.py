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
                # Mercados regionais com busca mais direta:
                {"nome": "Carrefour", "link": f"https://www.carrefour.com.br/busca/?q={t}"},
                {"nome": "Sonda", "link": f"https://www.sondadelivery.com.br/delivery/busca/{t}"},
                {"nome": "Tenda Atacadista", "link": f"https://www.tendaatacado.com.br/busca?q={t}"},
                {"nome": "D'avó", "link": f"https://www.davosupermercados.com.br/busca?q={t}"},
                {"nome": "Nagumo", "link": f"https://www.nagumodelivery.com.br/busca?q={t}"},
                {"nome": "Ricoy", "link": f"https://www.ricoy.com.br/busca?q={t}"},
                # Mantendo os grandes:
                {"nome": "Mercado Livre", "link": f"https://lista.mercadolivre.com.br/{t}"},
                {"nome": "Amazon", "link": f"https://www.amazon.com.br/s?k={t}"}
            ]
    return render_template("index.html", lojas=lojas, termo=termo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
