from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Isso evita o erro Not Found na página inicial
    return "Bem-vindo! Acesse /resultado para ver a comparação."

@app.route('/resultado')
def resultado():
    # É AQUI QUE VOCÊ ATUALIZA O TEXTO DA IA
    texto_da_ia = "O S23 Ultra é superior em produtividade com a S Pen e bateria, enquanto o iPhone 15 Pro oferece um desempenho de processamento inigualável e um ecossistema mais fechado e otimizado."
    
    return render_template('resultado.html', analise=texto_da_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
