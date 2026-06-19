import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        # Processa a comparação apenas se os dois campos estiverem preenchidos
        p1 = request.form.get('p1')
        p2 = request.form.get('p2')
        if p1 and p2:
            resultado = f"Análise Optimo: Comparando {p1} vs {p2}. O {p1} destaca-se pela inovação e performance, enquanto o {p2} oferece um melhor custo-benefício e durabilidade. A escolha ideal depende se você prioriza tecnologia de ponta ou economia a longo prazo."
            
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
