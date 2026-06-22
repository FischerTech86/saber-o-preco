from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Página inicial com o campo de busca
    return render_template('index.html')

@app.route('/comparar')
def comparar():
    # Captura os nomes dos produtos digitados pelo usuário
    p1 = request.args.get('produto1', 'Produto 1')
    p2 = request.args.get('produto2', 'Produto 2')
    
    # Aqui a IA seria chamada para preencher os dados técnicos automaticamente
    # Por enquanto, o layout está pronto para receber os dados
    return render_template('resultado.html', p1=p1, p2=p2)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
