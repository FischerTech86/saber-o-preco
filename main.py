from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    termo = request.args.get('pesquisa', 'Produto')
    
    # Como removemos a IA, vamos apenas exibir o termo que o usuário buscou
    # ou uma mensagem simples de confirmação.
    mensagem = f"Busca realizada para: {termo}. (O sistema de IA foi desativado conforme solicitado)."
    
    return render_template('resultado.html', termo=termo, lista=mensagem)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
