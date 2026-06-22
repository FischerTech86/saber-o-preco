from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Página inicial para evitar o erro "Not Found" no endereço principal
    return "Bem-vindo ao OPTIMO! Acesse /resultado para ver a comparação."

@app.route('/resultado')
def resultado():
    return render_template('resultado.html', 
                           nome_a="Smartphone Samsung Galaxy S23 Ultra", 
                           img_a="https://images.samsung.com/galaxy-s23-ultra.jpg", 
                           preco_a="R$ 5.999", 
                           specs_a="Tela 6.8', Snapdragon 8 Gen 2, 256GB",
                           
                           nome_b="Smartphone Apple iPhone 15 Pro", 
                           img_b="https://store.storeimages.cdn-apple.com/iphone-15-pro.jpg", 
                           preco_b="R$ 5.999", 
                           specs_b="Tela 6.1', Chip A17 Pro, 128GB",
                           
                           analise="O S23 Ultra é superior em produtividade e câmeras, enquanto o iPhone 15 Pro vence na integração de software.")

if __name__ == '__main__':
    # O Render usa a porta definida pelo sistema, por isso usamos os.environ.get
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
