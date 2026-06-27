from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analise = None
    prodA = None
    prodB = None
    
    if request.method == 'POST':
        # Captura os dados do formulário
        prodA = request.form.get('prodA')
        prodB = request.form.get('prodB')
        
        # Lógica de comparação (aqui você pode integrar com uma API futuramente)
        if prodA and prodB:
            analise = (f"Análise Comparativa: Comparando '{prodA}' com '{prodB}'. "
                       f"O {prodA} se destaca em usabilidade e design, enquanto o "
                       f"{prodB} apresenta um desempenho técnico superior em processamento. "
                       f"A escolha ideal depende se o seu foco é produtividade ou performance bruta.")
            
    return render_template('index.html', analise=analise, prodA=prodA, prodB=prodB)

@app.route('/dicas')
def dicas(): return render_template('dicas.html')

@app.route('/politica')
def politica(): return render_template('politica.html')

@app.route('/sobre')
def sobre(): return render_template('sobre.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
