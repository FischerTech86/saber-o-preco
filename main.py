from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mercados = []
    lojas = []
    termo = request.form.get("produto", "")

    if termo:
        # Mantemos o termo original para as outras lojas
        # Para o Sonda, vamos usar um formato que eles costumam aceitar melhor
        mercados = [
            {"nome": "Carrefour", "link": f"https://www.carrefour.com.br/busca/?q={termo.replace(' ', '%20')}"},
            {"nome": "Sonda", "link": f"https://www.sondadelivery.com.br/delivery/busca/{termo.replace(' ', '-')}"},
            {"nome": "Tenda", "link": f"https://www.tendaatacado.com.br/busca?q={termo.replace(' ', '%20')}"}
        ]
        lojas = [
            {"nome": "Mercado Livre", "link": f"https://lista.mercadolivre.com.br/search?q={termo.replace(' ', '%20')}"},
            {"nome": "Amazon", "link": f"https://www.amazon.com.br/s?k={termo.replace(' ', '+')}"}
        ]
        
    return render_template("index.html", mercados=mercados, lojas=lojas, termo=termo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
