from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/resultado')
def resultado():
    # Esta é a análise da IA que vai aparecer no seu site
    texto_da_ia = "O S23 Ultra é superior em produtividade e bateria, enquanto o iPhone 15 Pro vence na integração de software."
    return render_template('resultado.html', analise=texto_da_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
