from flask import Flask, render_template, request

app = Flask(__name__)

# Buscadores globais
GERAIS = [
    {"nome": "Mercado Livre", "link": "https://lista.mercadolivre.com.br/{t}"},
    {"nome": "Amazon", "link": "https://www.amazon.com.br/s?k={t}"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    apps = [
        {"nome": "Mercados", "icone": "🛒", "link": "/mercados"},
        {"nome": "Carros", "icone": "🚗", "link": "/carros"},
        {"nome": "Relógios", "icone": "⌚", "link": "/relogios"}
    ]
    return render_template("index.html", apps=apps)

@app.route("/<categoria>", methods=["GET", "POST"])
def buscar(categoria):
    links_especificos = {
        "mercados": [
            {"nome": "Carrefour", "link": "https://www.carrefour.com.br/busca/?q={t}"},
            {"nome": "Sonda", "link": "https://www.sondadelivery.com.br/delivery/busca/{t}"},
            {"nome": "Tenda", "link": "https://www.tendaatacado.com.br/busca?q={t}"}
        ],
        "carros": [
            {"nome": "Webmotors", "link": "https://www.webmotors.com.br/carros/estoque/?q={t}"},
            {"nome": "OLX", "link": "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/q/{t}"}
        ],
        "relogios": [
            {"nome": "Vivara", "link": "https://www.vivara.com.br/busca?q={t}"},
            {"nome": "Magalu", "link": "https://www.magazineluiza.com.br/busca/{t}/"}
        ]
    }
    
    termo = request.form.get("produto", "")
    lista_lojas = []
    
    if termo:
        t = termo.replace(" ", "%20")
        lista_lojas = links_especificos.get(categoria, []) + GERAIS
        for loja in lista_lojas:
            loja["url_final"] = loja["link"].replace("{t}", t)
            
    return render_template("categorias.html", titulo=categoria.capitalize(), lojas=lista_lojas, termo=termo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
