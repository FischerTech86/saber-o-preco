import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Simulação de base de dados
PRODUTOS_DB = {
    "carro": "https://www.webmotors.com.br",
    "relogio": "https://www.vivara.com.br",
    "mercado": "https://www.carrefour.com.br" 
}

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_busca = None
    resposta_ia = None

    if request.method == 'POST':
        # Busca de produtos
        produto = request.form.get('produto', '').lower()
        if produto:
            resultado_busca = PRODUTOS_DB.get(produto, "https://www.google.com/search?q=" + produto)
        
        # Resposta da IA
        pergunta = request.form.get('pergunta_ia')
        if pergunta:
            resposta_ia = "A IA Optimo sugere pesquisar em grandes lojas de varejo para este item."

    return render_template('index.html', resultado=resultado_busca, resposta=resposta_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
