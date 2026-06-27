from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ia', methods=['GET', 'POST'])
def ia():
    analise = None
    prodA = ""
    prodB = ""
    
    if request.method == 'POST':
        # Captura os dados do formulário
        prodA = request.form.get('prodA', '')
        prodB = request.form.get('prodB', '')
        
        # Lógica de análise (Aqui no futuro você conectará com a API da IA)
        if prodA and prodB:
            analise = f"Análise Comparativa: Comparando '{prodA}' com '{prodB}'. Ambos possuem características distintas. O {prodA} tende a oferecer uma performance sólida, enquanto o {prodB} destaca-se pela ergonomia e design. A melhor escolha depende da sua prioridade de uso."
        else:
            analise = "Por favor, preencha os dois produtos para realizar a comparação."

    return render_template('ia.html', analise=analise, prodA=prodA, prodB=prodB)

# Outras rotas (dicas, politica, sobre)
@app.route('/dicas')
def dicas(): return render_template('dicas.html')
@app.route('/politica')
def politica(): return render_template('politica.html')
@app.route('/sobre')
def sobre(): return render_template('sobre.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
