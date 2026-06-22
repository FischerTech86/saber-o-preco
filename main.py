from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Aqui é onde sua barra de pesquisa vai ficar
    return render_template('index.html') 

@app.route('/resultado')
def resultado():
    # Esta é a análise da sua IA que já estava funcionando
    analise_ia = "O S23 Ultra é superior em tela e bateria, enquanto o iPhone 15 Pro vence na integração de software."
    return render_template('resultado.html', analise=analise_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
