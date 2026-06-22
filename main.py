from flask import Flask, render_template
import os

app = Flask(__name__)

# Rota principal para evitar o erro 404 na raiz
@app.route('/')
def home():
    return "Servidor online! Acesse /resultado para ver a comparação."

# Rota de resultado que usa o arquivo na pasta templates/
@app.route('/resultado')
def resultado():
    # Defina aqui a análise da sua IA
    analise_ia = "O S23 Ultra é superior em tela e bateria, enquanto o iPhone 15 Pro vence na integração de software."
    
    return render_template('resultado.html', analise=analise_ia)

if __name__ == '__main__':
    # O Render atribui uma porta automaticamente
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
