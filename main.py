from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure a sua chave aqui
genai.configure(api_key="COLE_SUA_API_KEY_AQUI")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    p1 = request.args.get('produto1')
    p2 = request.args.get('produto2')
    
    # Pergunta para a IA buscar os dados
    prompt = f"Crie uma ficha técnica comparativa em formato de lista simples para: {p1} e {p2}. Inclua: Preço, Tela, Bateria, Câmera e Processador. Depois faça um resumo comparativo."
    
    response = model.generate_content(prompt)
    analise_completa = response.text
    
    return render_template('resultado.html', p1=p1, p2=p2, analise=analise_completa)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
