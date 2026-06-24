from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

# Configuração da chave de API vinda das variáveis de ambiente do Render
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    p1 = request.args.get('produto1', 'Produto 1')
    p2 = request.args.get('produto2', 'Produto 2')
    
    prompt = f"Crie um comparativo técnico entre {p1} e {p2}. Liste: Preço, Tela, Bateria, Câmera e Processador, seguido de um resumo final."
    
    try:
        response = model.generate_content(prompt)
        analise = response.text
    except Exception:
        analise = "Erro ao conectar com a IA. Verifique sua chave API no Render."
    
    return render_template('resultado.html', p1=p1, p2=p2, analise=analise)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
