from flask import Flask, render_template, request

app = Flask(__name__)

# Exemplo de como estruturar seus dados
LISTA_MERCADOS = [
    {"nome": "Carrefour", "link": "https://www.carrefour.com.br"},
    {"nome": "Tenda", "link": "https://www.tendaatacado.com.br"}
]

LISTA_LOJAS = [
    {"nome": "Mercado Livre", "link": "https://www.mercadolivre.com.br"},
    {"nome": "Amazon", "link": "https://www.amazon.com.br"}
]

LISTA_CARROS = [
    {"nome": "Webmotors", "link": "https://www.webmotors.com.br"},
    {"nome": "OLX Carros", "link": "https://www.olx.com.br/autos"}
]

LISTA_RELOGIOS = [
    {"nome": "Vivara", "link": "https://www.vivara.com.br"},
    {"nome": "Amazon Relógios", "link": "https://www.amazon.com.br/relogios"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    resposta_ia = ""
    produto_busca = ""
    
    if request.method == 'POST':
        # Aqui entra a sua lógica de IA
        if 'pergunta_ia' in request.form:
            resposta_ia = "Aqui está a resposta da sua pergunta à IA!"
        
        if 'produto' in request.form:
            produto_busca = request.form.get('produto')

    # É AQUI QUE O MAIN.PY MANDA OS DADOS PARA O HTML
    return render_template('index.html', 
                           resposta_ia=resposta_ia, 
                           produto=produto_busca,
                           mercados=LISTA_MERCADOS, 
                           lojas=LISTA_LOJAS, 
                           carros=LISTA_CARROS, 
                           relogios=LISTA_RELOGIOS)

if __name__ == '__main__':
    app.run(debug=True)
