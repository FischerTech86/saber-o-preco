from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    produto = request.args.get('produto', 'Produto não especificado')
    # Aqui a IA processaria o nome do produto
    analise_ia = f"Análise detalhada para: {produto}. O mercado oferece diversas opções, focando em custo-benefício e especificações técnicas específicas."
    return render_template('resultado.html', produto=produto, analise=analise_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
