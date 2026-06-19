import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    query = None
    if request.method == 'POST':
        query = request.form.get('produto', '').strip()
    return render_template('index.html', query=query)

if __name__ == '__main__':
    # Obtém a porta do ambiente ou usa 5000 como padrão
    port = int(os.environ.get('PORT', 5000))
    # O host deve ser 0.0.0.0 para aceitar conexões externas no Render
    app.run(host='0.0.0.0', port=port)
