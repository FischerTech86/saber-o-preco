from flask import Flask, render_template
import os

app = Flask(__name__)

# Esta rota redireciona o usuário direto para a comparação
@app.route('/')
def home():
    return '<meta http-equiv="refresh" content="0; url=/resultado">'

@app.route('/resultado')
def resultado():
    # Análise da IA
    analise_ia = "O S23 Ultra é superior em tela e bateria, enquanto o iPhone 15 Pro vence na integração de software."
    
    # O Flask buscará resultado.html dentro da pasta templates/
    return render_template('resultado.html', analise=analise_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
