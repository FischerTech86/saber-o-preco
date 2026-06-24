from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    p1 = request.args.get('produto1')
    p2 = request.args.get('produto2')
    
    # Pedimos para a IA separar os dados técnicos de forma estruturada
    prompt = f"""
    Crie uma ficha técnica comparativa para: {p1} e {p2}.
    Para CADA produto, forneça apenas: Preço, Tela, Processador, Armazenamento e Câmera.
    Depois, forneça um 'Veredito Geral' e 'Recomendação' como na imagem original.
    Formate a resposta para que eu possa exibir em cards separados.
    """
    
    try:
        response = model.generate_content(prompt)
        analise = response.text
    except Exception:
        analise = "Erro ao buscar dados."
    
    return render_template('resultado.html', p1=p1, p2=p2, analise=analise)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
