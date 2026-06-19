import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        p1 = request.form.get('p1')
        p2 = request.form.get('p2')
        if p1 and p2:
            resultado = f"Análise Optimo: Comparando {p1} vs {p2}. O {p1} destaca-se pela inovação, enquanto o {p2} oferece um melhor custo-benefício."
    return render_template('index.html', resultado=resultado)

# Rotas das páginas extras
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/dicas')
def dicas():
    return render_template('dicas.html')

@app.route('/politica-privacidade')
def politica():
    return render_template('politica.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
