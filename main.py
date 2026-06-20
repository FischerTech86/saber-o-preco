import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Adicione as outras rotas (sobre, dicas, etc) conforme necessário
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
