from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analise = None
    if request.method == 'POST':
        prod_a = request.form.get('prod_a')
        prod_b = request.form.get('prod_b')
        
        # Como tiramos a IA, o site agora reconhece os produtos 
        # mas não tenta processá-los externamente.
        if prod_a and prod_b:
            analise = f"Produtos recebidos: Comparando <strong>{prod_a}</strong> e <strong>{prod_b}</strong>. (Sistema local ativo)."
            
    return render_template('index.html', analise=analise)

if __name__ == '__main__':
    app.run()
