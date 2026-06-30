from flask import Flask, render_template, request

app = Flask(__name__)

# Dados básicos para o sistema
info = {
    "dicas": ["Verifique o frete antes de comprar.", "Olhe a avaliação da loja."],
    "politica": "O Optimo facilita sua busca de forma rápida e segura."
}

@app.route('/', methods=['GET', 'POST'])
def index():
    termo = ""
    if request.method == 'POST':
        termo = request.form.get('query', '').strip()
    return render_template('index.html', termo=termo, info=info)

if __name__ == '__main__':
    app.run(debug=True)
