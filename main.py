from flask import Flask, render_template, request

app = Flask(__name__)

# Banco de dados simulado mais rico
db_produtos = {
    "iphone 15 pro": {
        "Categoria": "Smartphone",
        "Tela": "6.1 Super Retina XDR",
        "Processador": "A17 Pro",
        "Câmera": "48MP Principal",
        "Bateria": "Até 23h de vídeo"
    },
    "galaxy s23 ultra": {
        "Categoria": "Smartphone",
        "Tela": "6.8 Dynamic AMOLED 2X",
        "Processador": "Snapdragon 8 Gen 2",
        "Câmera": "200MP Principal",
        "Bateria": "5000 mAh"
    },
    "geladeira brastemp": {
        "Categoria": "Eletrodoméstico",
        "Capacidade": "443 Litros",
        "Tipo": "Frost Free",
        "Eficiência": "A+++"
    }
}

def obter_dados_produto(nome):
    # Procura no nosso banco de dados
    nome_limpo = nome.lower()
    return db_produtos.get(nome_limpo, {
        "Status": "Produto não encontrado no banco de dados local.",
        "Dica": "Tente buscar por 'iPhone 15 Pro', 'Galaxy S23 Ultra' ou 'Geladeira Brastemp' para testar."
    })

@app.route('/', methods=['GET', 'POST'])
def index():
    dados_a = None
    dados_b = None
    nome_a = ""
    nome_b = ""

    if request.method == 'POST':
        nome_a = request.form.get('prodA')
        nome_b = request.form.get('prodB')
        
        dados_a = obter_dados_produto(nome_a)
        dados_b = obter_dados_produto(nome_b)

    return render_template('index.html', dados_a=dados_a, dados_b=dados_b, nome_a=nome_a, nome_b=nome_b)

if __name__ == '__main__':
    app.run(debug=True)
