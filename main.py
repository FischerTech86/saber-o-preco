from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/ia', methods=['GET', 'POST'])
def ia():
    analise = None
    prodA = ""
    prodB = ""
    
    if request.method == 'POST':
        prodA = request.form.get('prodA')
        prodB = request.form.get('prodB')
        
        # Aqui é onde a mágica acontece. 
        # Em breve, você trocará esse texto por uma chamada de API (OpenAI/Gemini)
        analise = f"Análise Comparativa: Comparando '{prodA}' com '{prodB}'. O {prodA} apresenta um custo-benefício mais atrativo, enquanto o {prodB} oferece maior durabilidade. Para o seu dia a dia, a melhor opção é o {prodA}."

    return render_template('ia.html', analise=analise, prodA=prodA, prodB=prodB)

# --- Suas outras rotas (index, dicas, etc) continuam aqui ---
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
