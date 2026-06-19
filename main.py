import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

# Dicionário de busca simples
DB = {
    "carro": "https://www.webmotors.com.br",
    "relogio": "https://www.vivara.com.br",
    "mercado": "https://www.carrefour.com.br"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Redirecionamento direto para evitar erros de renderização
        produto = request.form.get('produto', '').lower()
        if produto in DB:
            return redirect(DB[produto])
        return render_template('index.html', msg="Produto não encontrado.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
