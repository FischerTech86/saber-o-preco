from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    termo = request.args.get('pesquisa', 'Produto')
    
    # Como removemos a IA, vamos criar uma lista de "exemplo" 
    # para o site ter algo para mostrar.
    # Você pode alterar esses dados aqui abaixo:
    lista_de_produtos = [
        {'nome': f'{termo} Marca A', 'preco': 'R$ 10,00', 'dif': 'Melhor preço', 'link': f'https://www.google.com/search?q={termo.replace(" ", "+")}+marca+a&tbm=shop'},
        {'nome': f'{termo} Marca B', 'preco': 'R$ 15,00', 'dif': 'Melhor qualidade', 'link': f'https://www.google.com/search?q={termo.replace(" ", "+")}+marca+b&tbm=shop'},
    ]
    
    return render_template('resultado.html', termo=termo, lista=lista_de_produtos)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
