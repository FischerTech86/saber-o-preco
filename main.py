from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Captura tanto a busca quanto os produtos da comparação
    termo = request.form.get('query')
    prod_a = request.form.get('prod_a')
    prod_b = request.form.get('prod_b')
    
    # Se alguém fez busca OU comparou, termo_busca não será None
    termo_busca = termo or (f"{prod_a} vs {prod_b}" if prod_a and prod_b else None)
    
    return render_template('index.html', termo=termo_busca)

if __name__ == '__main__':
    app.run(debug=True)
