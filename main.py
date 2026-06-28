from flask import Flask, render_template, request

app = Flask(__name__)

# Aqui é onde o seu site "sabe" o que responder
banco_produtos = {
    "iphone 15": {
        "titulo": "iPhone 15",
        "desc": "Apple A16 Bionic, 128GB, Tela 6.1",
        "link": "https://www.google.com/search?tbm=shop&q=iphone+15"
    },
    "galaxy s23": {
        "titulo": "Samsung Galaxy S23",
        "desc": "Snapdragon 8 Gen 2, 256GB, Câmera 50MP",
        "link": "https://www.google.com/search?tbm=shop&q=galaxy+s23"
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    termo = ""
    
    if request.method == 'POST':
        termo = request.form.get('query', '').lower().strip()
        # Procura no banco de dados
        resultado = banco_produtos.get(termo)
    
    return render_template('index.html', resultado=resultado, termo=termo)

if __name__ == '__main__':
    app.run(debug=True)
