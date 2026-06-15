from flask import Flask, render_template, request

app = Flask(__name__)

# Configuração dos buscadores
GERAIS = [
    {"nome": "Mercado Livre", "link": "https://lista.mercadolivre.com.br/{t}"},
    {"nome": "Amazon", "link": "https://www.amazon.com.br/s?k={t}"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    apps = [
        {"nome": "Mercados", "link": "/mercados"},
        {"nome": "Carros", "link": "/carros"},
        {"nome": "Relogios", "link": "/relogios"}
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
        # Pega a lista da categoria OU uma lista vazia se a categoria não existir
        lista_lojas = links_especificos.get(categoria.lower(), []) + GERAIS
        for loja in lista_lojas:
            loja["url_final"] = loja["link"].replace("{t}", t)
            
    return render_template("categorias.html", titulo=categoria.capitalize(), lojas=lista_lojas, termo=termo)

if __name__ == "__main__":
    app.run()
