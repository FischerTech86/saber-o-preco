from flask import Flask, render_template, request

app = Flask(__name__)

def gerar_resumo_ia(termo):
    termo = termo.lower()
    if "motorola" in termo and "xiaomi" in termo:
        return "Motorola: Ponto positivo é a interface limpa e boa assistência no Brasil; negativo é o custo-benefício em modelos topo de linha. Xiaomi: Ponto positivo é o hardware potente por preço baixo; negativo é a interface (MIUI) carregada de propagandas."
    if "carro" in termo:
        return "Dica: Ao comprar um carro, sempre verifique o histórico de manutenção, quilometragem e se há leilões no histórico do chassi."
    return ""

@app.route("/", methods=["GET", "POST"])
def index():
    termo = request.form.get("produto", "")
    mercados = []
    lojas = []
    carros = []
    relogios = []
    ia_resumo = ""

    if termo:
        ia_resumo = gerar_resumo_ia(termo)
        t = termo.replace(" ", "+")
        
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
        
    return render_template("index.html", mercados=mercados, lojas=lojas, carros=carros, relogios=relogios, termo=termo, ia=ia_resumo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
