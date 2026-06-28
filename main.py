from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Simulação de Banco de Dados (Isso aqui seria uma API de produtos no futuro)
db_produtos = {
    "galaxy s23 ultra": {"Preço": "R$ 5.999", "Tela": "6.8\" QHD+", "Processador": "Snapdragon 8 Gen 2", "Câmera": "200MP"},
    "iphone 15 pro": {"Preço": "R$ 6.999", "Tela": "6.1\" OLED", "Processador": "A17 Pro", "Câmera": "48MP"}
}

@app.route('/', methods=['GET', 'POST'])
def index():
    dados_a = None
    dados_b = None
    analise = None

    if request.method == 'POST':
        nome_a = request.form.get('prodA').lower()
        nome_b = request.form.get('prodB').lower()
        
        # Busca os dados no dicionário
        dados_a = db_produtos.get(nome_a, {"Status": "Produto não encontrado"})
        dados_b = db_produtos.get(nome_b, {"Status": "Produto não encontrado"})
        
        # Gera uma análise baseada nos dados
        if "Preço" in dados_a and "Preço" in dados_b:
            analise = f"Comparação entre {nome_a.upper()} e {nome_b.upper()}: O primeiro foca em {dados_a.get('Processador')}, enquanto o segundo utiliza {dados_b.get('Processador')}."
        else:
            analise = "Não foi possível realizar uma comparação técnica detalhada com os nomes fornecidos. Tente 'Galaxy S23 Ultra' ou 'iPhone 15 Pro'."

    return render_template('index.html', dados_a=dados_a, dados_b=dados_b, analise=analise)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
