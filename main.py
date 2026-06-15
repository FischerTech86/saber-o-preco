from flask import Flask, render_template, request

app = Flask(__name__)

def responder_ia(p):
    if not p: return "Olá! Sou a IA Optimo. Como posso ajudar?"
    p = p.lower()
    
    # Aqui ficam as respostas. Se não encontrar, ele responde algo genérico.
    respostas = {
        "motorola": "Interface limpa, ótimo custo-benefício.",
        "xiaomi": "Hardware potente, preço baixo.",
        "iphone": "Ecossistema integrado, alta performance.",
        "samsung": "Telas incríveis, câmeras versáteis.",
        "notebook": "Priorize 8GB RAM e SSD.",
        "carro": "Verifique histórico de manutenção."
    }
    
    for chave in respostas:
        if chave in p:
            return respostas[chave]
            
    return "Entendido! O que mais deseja saber?"

@app.route("/", methods=["GET", "POST"])
def index():
    produto = request.form.get("produto", "")
    pergunta_ia = request.form.get("pergunta_ia", "")
    
    # A IA agora responde independente de haver busca de produto
    resposta_ia = responder_ia(pergunta_ia)
    
    mercados, lojas, carros, relogios = [], [], [], []

    if produto:
        t = produto.replace(" ", "%20")
        # ... (suas listas de links continuam aqui)
        
    return render_template("index.html", 
                           mercados=mercados, lojas=lojas, carros=carros, 
                           relogios=relogios, produto=produto, 
                           resposta_ia=resposta_ia)
