from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    link_google = None
    produto_nome = ""

    if request.method == 'POST':
        produto_nome = request.form.get('produto', '').strip()
        if produto_nome:
            # Formata o texto para o link do Google (substitui espaços por +)
            busca_formatada = produto_nome.replace(" ", "+")
            link_google = f"https://www.google.com/search?tbm=shop&q={busca_formatada}"

    return render_template('index.html', link=link_google, produto=produto_nome)

if __name__ == '__main__':
    app.run(debug=True)
