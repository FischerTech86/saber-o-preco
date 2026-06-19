import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    comparacao = None
    if request.method == 'POST':
        # Busca direta no Shopping
        if 'produto' in request.form and request.form.get('produto'):
            produto = request.form.get('produto', '').strip()
            return redirect(f"https://www.google.com/search?q={produto}&tbm=shop")
        
        # Comparador Tático
        if 'p1' in request.form and 'p2' in request.form:
            p1 = request.form.get('p1').strip()
            p2 = request.form.get('p2').strip()
            comparacao = f"Veredito Optimo: O {p1} é superior em performance bruta, enquanto o {p2} vence na autonomia de bateria e custo-benefício. A escolha depende se sua prioridade é tecnologia de ponta ou economia."
            
    return render_template('index.html', comparacao=comparacao)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
