from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    termo = request.args.get('pesquisa', '')
    lista = []
    if termo:
        busca_url = termo.replace(" ", "+")
        lista = [
            {'nome': f'{termo} Premium', 'dif': 'Alta qualidade e durabilidade', 'link': f'https://www.google.com/search?q={busca_url}+premium&tbm=shop'},
            {'nome': f'{termo} Padrão', 'dif': 'Equilíbrio ideal entre preço e qualidade', 'link': f'https://www.google.com/search?q={busca_url}+padrao&tbm=shop'},
            {'nome': f'{termo} Econômico', 'dif': 'Opção mais barata disponível', 'link': f'https://www.google.com/search?q={busca_url}+barato&tbm=shop'}
        ]
    return render_template('index.html', lista=lista)

@app.route('/ia', methods=['GET', 'POST'])
def ia():
    analise = None
    prodA = ""
    prodB = ""
    
    if request.method == 'POST':
        prodA = request.form.get('prodA')
        prodB = request.form.get('prodB')
        
        # Lógica de comparação
        if prodA and prodB:
            analise = f"Análise Comparativa: Comparando '{prodA}' e '{prodB}'. O {prodA} apresenta um custo-benefício atrativo, enquanto o {prodB} se destaca pela performance técnica. Recomendamos analisar o uso pretendido antes da compra."
    
    # IMPORTANTE: Enviando prodA e prodB de volta para o HTML
    return render_template('ia.html', analise=analise, prodA=prodA, prodB=prodB)

@app.route('/dicas')
def dicas(): return render_template('dicas.html')

@app.route('/politica')
def politica(): return render_template('politica.html')

@app.route('/sobre')
def sobre(): return render_template('sobre.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
