from flask import Flask, render_template, request

app = Flask(__name__)

def gerar_resumo_ia(termo):
    termo = termo.lower()
    
    # IA agora identifica modelos específicos e categorias
    if "motorola" in termo:
        if "edge" in termo:
            return "Linha Edge: Foco em design premium, câmeras avançadas e telas curvas de alta qualidade."
        return "Motorola: Conhecida pela interface limpa (quase Android puro) e excelente custo-benefício no Brasil."
    
    if "xiaomi" in termo or "poco" in termo or "redmi" in termo:
        return "Xiaomi: Foco total em custo-benefício, entregando hardware potente e câmeras com muitos recursos por um preço agressivo."
    
    if "iphone" in termo or "apple" in termo:
        return "iPhone/Apple: Foco em ecossistema integrado, alta performance, valor de revenda e atualizações por muitos anos."
    
    if "samsung" in termo or "galaxy" in termo:
        return "Samsung: Foco em telas incríveis (AMOLED), câmeras versáteis e a linha S, que compete no topo com os melhores."
    
    if "notebook" in termo or "laptop" in termo:
        return "Dica: Ao escolher um notebook, verifique o processador (i5/Ryzen 5 para uso geral), memória RAM (mínimo 8GB) e se o SSD é do tipo NVMe para maior velocidade."
    
    if "tablet" in termo:
        return "Dica: Tablets são ótimos para consumo de mídia e estudo. Verifique a resolução da tela e a compatibilidade com canetas stylus se for desenhar ou anotar."
    
    if "carro" in termo:
        return "Dica: Verifique sempre o histórico de manutenção, quilometragem e se há leilões no histórico do chassi."

    return "IA Optimo: Analisando seu produto... Procure sempre verificar a garantia oficial e opiniões de quem já comprou o modelo específico que você escolheu."

@app.route("/", methods=["GET", "POST"])
def index():
    termo = request.form.get("produto", "")
    mercados, lojas, carros, relogios, ia = [], [], [], [], None

    if termo:
        ia = gerar_resumo_ia(termo) # Chama a IA com o termo mais detalhado
        t = termo.replace(" ", "%20")
        
        # (Mantive a sua estrutura de lojas igual, apenas ajustada para o termo)
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
