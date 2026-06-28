from flask import Flask, render_template, request

app = Flask(__name__)

# Os dados estão aqui. O HTML vai ler exatamente este dicionário.
conteudo_extra = {
    "dicas": [
        "Verifique sempre a reputação do vendedor antes de comprar.",
        "Compare o valor do frete, às vezes o barato sai caro.",
        "Aproveite cupons de desconto na primeira compra."
    ],
    "politica": "O Optimo é uma ferramenta de busca que visa facilitar sua jornada de compra, garantindo transparência nos resultados."
}

@app.route('/', methods=['GET', 'POST'])
def index():
    termo = ""
    if request.method == 'POST':
        termo = request.form.get('query', '').strip()
    
    # Enviamos o dicionário 'conteudo_extra' como 'info' para o HTML
    return render_template('index.html', termo=termo, info=conteudo_extra)

if __name__ == '__main__':
    app.run(debug=True)
