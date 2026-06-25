from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    termo = request.args.get('pesquisa', '')
    lista = []
    
    if termo:
        busca = termo.replace(" ", "+")
        
        # A lista agora foca apenas no nome, diferencial e link
        lista = [
            {
                'nome': f'{termo} Premium',
                'dif': 'Alta qualidade e durabilidade',
                'link': f'https://www.google.com/search?q={busca}+premium&tbm=shop'
            },
            {
                'nome': f'{termo} Padrão',
                'dif': 'Equilíbrio ideal entre preço e qualidade',
                'link': f'https://www.google.com/search?q={busca}+padrao&tbm=shop'
            },
            {
                'nome': f'{termo} Econômico',
                'dif': 'Opção mais barata disponível',
                'link': f'https://www.google.com/search?q={busca}+barato&tbm=shop'
            }
        ]
    
    return render_template('index.html', termo=termo, lista=lista)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
