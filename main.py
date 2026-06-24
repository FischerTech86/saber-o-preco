from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

# Configuração segura usando variável de ambiente
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    p1 = request.args.get('produto1', 'Produto 1')
    p2 = request.args.get('produto2', 'Produto 2')
    
    # Prompt mais robusto
    prompt = f"Crie um comparativo técnico entre {p1} e {p2}. Forneça os dados em formato de lista (Preço, Tela, Bateria, Câmera e Processador) e um resumo final."
    
    try:
        response = model.generate_content(prompt)
        analise = response.text
    except Exception:
        analise = "Não foi possível carregar os dados. Verifique a API Key ou tente novamente."
    
    return render_template('resultado.html', p1=p1, p2=p2, analise=analise)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
