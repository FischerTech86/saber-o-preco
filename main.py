from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Rota para a página inicial (Busca)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de resultado
@app.route('/resultado')
def resultado():
    # Pega o que o usuário digitou
    p1 = request.args.get('produto1', 'Produto 1')
    p2 = request.args.get('produto2', 'Produto 2')
    
    # Análise fixa para garantir o funcionamento
    analise = f"Análise entre {p1} e {p2}: Ambos são excelentes, mas cada um atende a um perfil diferente."
    
    return render_template('resultado.html', p1=p1, p2=p2, analise=analise)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)