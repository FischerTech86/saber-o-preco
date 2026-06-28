from flask import Flask, render_template, request

app = Flask(__name__)

# Dados para as seções extras
conteudo_extra = {
    "dicas": [
        "Sempre verifique a reputação do vendedor.",
        "Compare o preço do frete antes de finalizar.",
        "Fique atento às promoções relâmpago."
    ],
    "politica": "Nossa política é ajudar você a encontrar o melhor preço de forma rápida, transparente e segura, sem coletar dados sensíveis."
}

@app.route('/', methods=['GET', 'POST'])
def index():
    termo = ""
    if request.method == 'POST':
        termo = request.form.get('query', '').strip()
    
    # Passando o conteudo_extra para o HTML
    return render_template('index.html', termo=termo, info=conteudo_extra)

if __name__ == '__main__':
    app.run(debug=True)
