from flask import Flask, render_template, request

app = Flask(__name__)

def gerar_resumo_ia(termo):
    termo = termo.lower()
    # Lógica da IA
    if "motorola" in termo and "xiaomi" in termo:
        return "Motorola: Foco em interface limpa e boa assistência técnica no Brasil. Xiaomi: Foco em hardware potente por preço baixo, mas interface mais carregada."
    if "carro" in termo:
        return "Dica: Ao comprar um carro, sempre verifique o histórico de manutenção, quilometragem e se há leilões no histórico do chassi."
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    termo = request.form.get("produto", "")
    mercados, lojas, carros, relogios, ia = [], [], [], [], None

    if termo:
        ia = gerar_resumo_ia(termo)
        t = termo.replace(" ", "%20")
        
        mercados = [
            {"nome": "Carrefour", "link": f"https://www.carrefour.com.br/busca/?q={t}"},
            {"nome": "Tenda", "link": f"https://www.tendaatacado.com.br/busca?q={t}"},
            {"nome": "Sonda", "link": f"https://www.sondadelivery.com.br/delivery/busca?termo={t}"}
        ]
        lojas = [
            {"nome": "Mercado Livre", "link": f"https://lista.mercadolivre.com.br/search?q={t}"},
            {"nome": "Amazon", "link": f"https://www.amazon.com.br/s?k={t}"},
            {"nome": "Magalu", "link": f"https://www.magazineluiza.com.br/busca/{t}/"},
            {"nome": "Shopee", "link": f"https://shopee.com.br/search?keyword={t}"}
        ]
        carros = [
            {"nome": "Webmotors", "link": f"https://www.webmotors.com.br/carros/estoque/?q={t}"},
            {"nome": "OLX", "link": f"https://www.olx.com.br/autos-e-pecas/carros/q/{t}"}
        ]
        relogios = [
            {"nome": "Vivara", "link": f"https://www.vivara.com.br/busca?q={t}"},
            {"nome": "Amazon Relógios", "link": f"https://www.amazon.com.br/s?k=relogio+{t}"}
        ]
        
    return render_template("index.html", mercados=mercados, lojas=lojas, carros=carros, relogios=relogios, termo=termo, ia=ia)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
