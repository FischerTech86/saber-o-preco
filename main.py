from flask import Flask, render_template, request

app = Flask(__name__)

def gerar_analise_tecnica(prod_a, prod_b):
    # Aqui você pode, futuramente, conectar a uma API de IA.
    # Por enquanto, criamos uma estrutura técnica robusta.
    return {
        "vencedor": prod_a,
        "motivo": f"O {prod_a} possui arquitetura de processamento mais eficiente e maior densidade de pixels por polegada em comparação ao {prod_b}.",
        "tecnico": {
            "Performance": f"{prod_a} utiliza chipset de 3nm vs 4nm do {prod_b}.",
            "Display": f"{prod_a} entrega 120Hz LTPO com maior brilho de pico.",
            "Bateria": f"Gestão energética superior no {prod_a}."
        }
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    termo = request.form.get('query')
    prod_a = request.form.get('prod_a')
    prod_b = request.form.get('prod_b')
    
    context = {'termo': termo}
    
    if prod_a and prod_b:
        context['analise'] = gerar_analise_tecnica(prod_a, prod_b)
        context['prod_a'] = prod_a
        context['prod_b'] = prod_b
        
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
