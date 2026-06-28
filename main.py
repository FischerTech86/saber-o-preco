from flask import Flask, render_template, request

app = Flask(__name__)

# Este é o seu banco de dados manual. É aqui que você cadastra seus produtos.
banco_de_dados = {
    "iphone 15": {
        "Tela": "6.1 OLED",
        "Processador": "A16 Bionic",
        "Câmera": "48 MP",
        "Bateria": "3349 mAh"
    },
    "galaxy s23": {
        "Tela": "6.1 Dynamic AMOLED",
        "Processador": "Snapdragon 8 Gen 2",
        "Câmera": "50 MP",
        "Bateria": "3900 mAh"
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    dados_a = None
    dados_b = None
    nome_a = ""
    nome_b = ""

    if request.method == 'POST':
        nome_a = request.form.get('prodA', '').lower().strip()
        nome_b = request.form.get('prodB', '').lower().strip()
        
        # Busca direta no dicionário (sem IA, sem complicações)
        dados_a = banco_de_dados.get(nome_a)
        dados_b = banco_de_dados.get(nome_b)

    return render_template('index.html', dados_a=dados_a, dados_b=dados_b, nome_a=nome_a, nome_b=nome_b)

if __name__ == '__main__':
    app.run(debug=True)
