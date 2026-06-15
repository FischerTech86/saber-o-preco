from flask import Flask, render_template, request

app = Flask(__name__)

def gerar_resumo_ia(termo):
    termo = termo.lower()
    
    # Dicionário de respostas curtas (máximo 5 palavras)
    respostas = {
        "motorola": "Interface limpa, ótimo custo-benefício.",
        "xiaomi": "Hardware potente, preço muito baixo.",
        "iphone": "Ecossistema integrado, alta performance.",
        "samsung": "Telas incríveis, câmeras versáteis.",
        "notebook": "Priorize 8GB RAM e SSD.",
        "tablet": "Ótimo para estudo e mídia.",
        "carro": "Verifique histórico de manutenção.",
        "iphone 15": "Câmera excelente, bateria boa.",
        "moto g84": "Melhor intermediário da Motorola."
    }

    # Procura se o termo existe nas nossas respostas curtas
    for chave in respostas:
        if chave in termo:
            return respostas[chave]
            
    return "Pesquise modelos específicos aqui."

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
