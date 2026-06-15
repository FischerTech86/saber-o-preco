from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# Rota obrigatória para o Google AdSense verificar o seu ads.txt
@app.route('/ads.txt')
def ads_txt():
    return send_from_directory('.', 'ads.txt')

def responder_ia(p):
    if not p: return "Olá! Sou a IA Optimo. Como posso ajudar?"
    p = p.lower()
    respostas = {
        "motorola": "Interface limpa, ótimo custo-benefício.",
        "xiaomi": "Hardware potente, preço baixo.",
        "iphone": "Ecossistema integrado, alta performance.",
        "samsung": "Telas incríveis, câmeras versáteis.",
        "notebook": "Priorize 8GB RAM e SSD.",
        "carro": "Verifique histórico de manutenção.",
        "relogio": "Modelos digitais oferecem mais funções."
    }
    for chave in respostas:
        if chave in p: return respostas[chave]
    return "Entendido! O que mais deseja saber?"

@app.route("/", methods=["GET", "POST"])
def index():
    produto = request.form.get("produto", "")
    pergunta_ia = request.form.get("pergunta_ia", "")
    resposta_ia = responder_ia(pergunta_ia)
    
    mercados, lojas, carros, relogios = [], [], [], []
    
    if produto:
        t = produto.replace(" ", "%20")
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
        
    return render_template("index.html", 
                           mercados=mercados, lojas=lojas, carros=carros, relogios=relogios,
                           produto=produto, resposta_ia=resposta_ia)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
