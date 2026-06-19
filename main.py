import os
from flask import Flask, render_template, request, redirect

# O Flask já procura a pasta 'static' automaticamente se ela estiver na raiz
app = Flask(__name__)

DB = {
    "carro": "https://www.webmotors.com.br",
    "relogio": "https://www.vivara.com.br",
    "mercado": "https://www.carrefour.com.br"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        produto = request.form.get('produto', '').lower()
        if produto in DB:
            return redirect(DB[produto])
        return render_template('index.html', msg="Produto não encontrado.")
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
