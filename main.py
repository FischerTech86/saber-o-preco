from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

# Configura a chave de forma segura através de variável de ambiente
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    p1 = request.args.get('produto1', 'Produto 1')
    p2 = request.args.get('produto2', 'Produto 2')
    
    # IA busca os dados
    prompt = f"Crie uma ficha técnica técnica curta e objetiva para os produtos: {p1} e {p2}. Liste apenas: Preço, Tela, Bateria, Câmera e Processador."
    
    try:
        response = model.generate_content(prompt)
        resultado_ia = response.text
    except Exception as e:
        resultado_ia = "Erro ao carregar dados da IA. Tente novamente."
    
    return render_template('resultado.html', p1=p1, p2=p2, analise=resultado_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
