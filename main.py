from flask import Flask, render_template, request

app = Flask(__name__)

# Configuração simples
@app.route("/", methods=["GET", "POST"])
def index():
    mercados = [
        {"nome": "Carrefour", "link": "https://www.carrefour.com.br/busca/?q={t}"},
        {"nome": "Sonda", "link": "https://www.sondadelivery.com.br/delivery/busca/{t}"},
        {"nome": "Tenda", "link": "https://www.tendaatacado.com.br/busca?q={t}"}
    ]
    lojas = [
        {"nome": "Mercado Livre", "link": "https://lista.mercadolivre.com.br/{t}"},
        {"nome": "Amazon", "link": "https://www.amazon.com.br/s?k={t}"}
    ]
    
    termo = request.form.get("produto", "")
    if termo:
        t = termo.replace(" ", "%20")
        for m in mercados: m["link"] = m["link"].replace("{t}", t)
        for l in lojas: l["link"] = l["link"].replace("{t}", t)
        
    return render_template("index.html", mercados=mercados, lojas=lojas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
