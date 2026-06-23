from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Página inicial com a barra de busca
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    # Captura os dados da busca
    produto1 = request.args.get('produto1', 'Produto 1')
    produto2 = request.args.get('produto2', 'Produto 2')
    
    # Simulação da análise da IA
    analise = f"Comparação realizada entre {produto1} e {produto2}. Ambos são excelentes opções, dependendo do seu foco em custo ou desempenho."
    
    return render_template('resultado.html', p1=produto1, p2=produto2, analise=analise)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
