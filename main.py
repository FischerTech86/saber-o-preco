from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Esta linha define a rota da página inicial
@app.route('/')
def index():
    # 1. Captura o que o usuário digitou
    termo = request.args.get('pesquisa', '')
    lista = []
    
    # 2. Se tiver pesquisa, cria a lista (a lógica de busca)
    if termo:
        busca = termo.replace(" ", "+")
        lista = [
            {'nome': f'{termo} Premium', 'dif': 'Alta qualidade', 'link': f'https://www.google.com/search?q={busca}+premium&tbm=shop'},
            {'nome': f'{termo} Padrão', 'dif': 'Equilíbrio', 'link': f'https://www.google.com/search?q={busca}+padrao&tbm=shop'},
            {'nome': f'{termo} Econômico', 'dif': 'Preço baixo', 'link': f'https://www.google.com/search?q={busca}+barato&tbm=shop'}
        ]
    
    # 3. Aqui é onde entra a linha que você mandou!
    # Ela "entrega" as variáveis para o seu arquivo HTML.
    return render_template('index.html', termo=termo, lista=lista)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
