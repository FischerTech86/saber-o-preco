import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Dados
LISTA_MERCADOS = [{"nome": "Carrefour", "link": "https://www.carrefour.com.br"}, {"nome": "Tenda", "link": "https://www.tendaatacado.com.br"}]
LISTA_LOJAS = [{"nome": "Mercado Livre", "link": "https://www.mercadolivre.com.br"}, {"nome": "Amazon", "link": "https://www.amazon.com.br"}]
LISTA_CARROS = [{"nome": "Webmotors", "link": "https://www.webmotors.com.br"}, {"nome": "OLX Carros", "link": "https://www.olx.com.br/autos"}]
LISTA_RELOGIOS = [{"nome": "Vivara", "link": "https://www.vivara.com.br"}, {"nome": "Amazon Relógios", "link": "https://www.amazon.com.br/relogios"}]

@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializa como None para não aparecer nada na tela
    resultados = None
    
    if request.method == 'POST':
        # Se buscar produto, mostra as categorias
        if 'produto' in request.form and request.form.get('produto'):
            resultados = {
                'mercados': LISTA_MERCADOS,
                'lojas': LISTA_LOJAS,
                'carros': LISTA_CARROS,
                'relogios': LISTA_RELOGIOS
            }
        # Se perguntar à IA, você processaria aqui (simulado)
        elif 'pergunta_ia' in request.form:
            resultados = {'ia_resposta': "Resultado da sua pergunta processado pela IA Optimo."}

    return render_template('index.html', res=resultados)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
