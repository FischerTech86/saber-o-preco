from flask import Flask, render_template, request

app = Flask(__name__)

# Esta função "finge" ser uma IA que conhece todos os produtos
def gerar_ficha_tecnica(nome_produto):
    # Aqui você conectaria uma API real (como Gemini ou OpenAI) futuramente
    return {
        "Categoria": "Eletrônicos/Geral",
        "Destaque": "Produto de alta performance",
        "Durabilidade": "Alta",
        "Custo-benefício": "Requer análise de mercado"
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    dados_a = None
    dados_b = None
    analise = None
    nome_a = ""
    nome_b = ""

    if request.method == 'POST':
        nome_a = request.form.get('prodA')
        nome_b = request.form.get('prodB')
        
        # Gera dados para qualquer nome que for digitado
        dados_a = gerar_ficha_tecnica(nome_a)
        dados_b = gerar_ficha_tecnica(nome_b)
        
        analise = f"Comparação automática entre {nome_a} e {nome_b}: O foco principal é verificar a compatibilidade técnica. {nome_a} apresenta características de mercado robustas, enquanto {nome_b} é uma alternativa competitiva. Recomendamos comparar os preços atuais em marketplaces."

    return render_template('index.html', dados_a=dados_a, dados_b=dados_b, analise=analise, nome_a=nome_a, nome_b=nome_b)

if __name__ == '__main__':
    app.run(debug=True)
