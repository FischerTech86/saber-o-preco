from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Variáveis para a Busca
    termo = request.args.get('pesquisa', '')
    lista_busca = []
    
    # Variáveis para a Comparação
    analise = None
    prodA = None
    prodB = None

    # Lógica da Busca (GET)
    if termo:
        busca_url = termo.replace(" ", "+")
        lista_busca = [
            {'nome': f'{termo} Premium', 'dif': 'Alta qualidade', 'link': f'https://www.google.com/search?q={busca_url}+premium&tbm=shop'},
            {'nome': f'{termo} Padrão', 'dif': 'Equilíbrio ideal', 'link': f'https://www.google.com/search?q={busca_url}+padrao&tbm=shop'},
            {'nome': f'{termo} Econômico', 'dif': 'Melhor preço', 'link': f'https://www.google.com/search?q={busca_url}+barato&tbm=shop'}
        ]

    # Lógica da Comparação (POST)
    if request.method == 'POST':
        prodA = request.form.get('prodA')
        prodB = request.form.get('prodB')
        if prodA and prodB:
            analise = f"Análise Comparativa: O {prodA} e {prodB} foram analisados. Recomendamos focar em custo-benefício se o uso for casual, ou performance se for profissional."

    return render_template('index.html', lista=lista_busca, analise=analise, prodA=prodA, prodB=prodB)

# Outras rotas
@app.route('/dicas')
def dicas(): return render_template('dicas.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
