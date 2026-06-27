from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de IA (Comparação de produtos)
@app.route('/ia', methods=['GET', 'POST'])
def ia():
    analise = None
    prodA = ""
    prodB = ""
    
    if request.method == 'POST':
        prodA = request.form.get('prodA', '')
        prodB = request.form.get('prodB', '')
        
        if prodA and prodB:
            # Aqui você poderá, no futuro, conectar a API da IA real
            analise = f"Análise Comparativa: Comparando '{prodA}' com '{prodB}'. O {prodA} apresenta características robustas, enquanto o {prodB} se destaca pela eficiência e preço. Recomendamos avaliar suas prioridades antes de decidir."
        else:
            analise = "Por favor, preencha o nome dos dois produtos para realizar a comparação."
            
    return render_template('ia.html', analise=analise, prodA=prodA, prodB=prodB)

# Rota para Dicas
@app.route('/dicas')
def dicas():
    return render_template('dicas.html')

# Rota para Política
@app.route('/politica')
def politica():
    return render_template('politica.html')

# Rota para Sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    # Configuração para rodar no Render (ou localmente)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
