from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    termo = request.args.get('pesquisa', '')
    lista = []
    if termo:
        busca = termo.replace(" ", "+")
        lista = [
            {'nome': f'{termo} Premium', 'dif': 'Alta qualidade', 'link': f'https://www.google.com/search?q={busca}+premium&tbm=shop'},
            {'nome': f'{termo} Padrão', 'dif': 'Equilíbrio', 'link': f'https://www.google.com/search?q={busca}+padrao&tbm=shop'},
            {'nome': f'{termo} Econômico', 'dif': 'Preço baixo', 'link': f'https://www.google.com/search?q={busca}+barato&tbm=shop'}
        ]
    return render_template('index.html', termo=termo, lista=lista)

@app.route('/dicas')
def dicas(): return render_template('dicas.html')

@app.route('/politica')
def politica(): return render_template('politica.html')

@app.route('/sobre')
def sobre(): return render_template('sobre.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
