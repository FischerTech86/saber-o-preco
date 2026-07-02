from flask import Flask, render_template, request

app = Flask(__name__)

# Rota da página inicial (index.html)
@app.route('/', methods=['GET', 'POST'])
def index():
    termo = ""
    if request.method == 'POST':
        termo = request.form.get('query', '').strip()
    return render_template('index.html', termo=termo)

# Rota para Dicas (dicas.html)
@app.route('/dicas')
def dicas():
    return render_template('dicas.html')

# Rota para Política (politica.html)
@app.route('/politica')
def politica():
    return render_template('politica.html')

# Rota para Sobre (sobre.html)
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)
