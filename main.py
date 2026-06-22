from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/resultado')
def resultado():
    # Análise fixa para manter a consistência do visual aprovado
    analise_ia = "O S23 Ultra é superior em tela e bateria, enquanto o iPhone 15 Pro vence na integração de software."
    return render_template('resultado.html', analise=analise_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
