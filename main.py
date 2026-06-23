from flask import Flask, render_template
import os

app = Flask(__name__)

# Esta rota renderiza o resultado da comparação
@app.route('/resultado')
def resultado():
    # Esta variável 'analise' é o que aparece na caixa da IA
    analise_ia = "O S23 Ultra é superior em tela e bateria, enquanto o iPhone 15 Pro vence na integração de software."
    return render_template('resultado.html', analise=analise_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
