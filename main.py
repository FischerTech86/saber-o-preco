from flask import Flask, render_template, request

app = Flask(__name__)

# Seu banco de dados simples. 
# Adicione os produtos que quiser aqui.
produtos = {
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
    resultado_a = None
    resultado_b = None
    nome_a = ""
    nome_b = ""
    
    if request.method == 'POST':
        nome_a = request.form.get('prodA', '').lower().strip()
        nome_b = request.form.get('prodB', '').lower().strip()
        
        # Busca direta, se não achar, fica None
        resultado_a = produtos.get(nome_a)
        resultado_b = produtos.get(nome_b)
        
    return render_template('index.html', 
                           resultado_a=resultado_a, 
                           resultado_b=resultado_b, 
                           nome_a=nome_a, 
                           nome_b=nome_b)

if __name__ == '__main__':
    app.run(debug=True)
