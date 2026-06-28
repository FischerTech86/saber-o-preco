from flask import Flask, render_template, request
import requests # Esta biblioteca faz a busca na internet

app = Flask(__name__)

# Esta função substitui o dicionário manual
def buscar_info_real(nome_produto):
    # Aqui entraria a conexão com uma API (ex: SerpApi ou Google Custom Search)
    # Exemplo de lógica:
    # 1. Monta a URL de busca
    # 2. Faz o request.get()
    # 3. Extrai as especificações da resposta JSON
    
    # Exemplo de como a função deveria retornar (Simulando uma resposta da API):
    return {
        "Processador": "Dados buscados via API...",
        "Tela": "Dados buscados via API...",
        "Bateria": "Dados buscados via API..."
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome_a = request.form.get('prodA')
        nome_b = request.form.get('prodB')
        
        # Agora, em vez de olhar no dicionário fixo, 
        # nós chamamos a função que busca na internet
        dados_a = buscar_info_real(nome_a)
        dados_b = buscar_info_real(nome_b)
        
        return render_template('index.html', dados_a=dados_a, dados_b=dados_b, nome_a=nome_a, nome_b=nome_b)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
