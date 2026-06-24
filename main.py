from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)
# Certifique-se de que a variável GOOGLE_API_KEY esteja configurada no Render
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    p1 = request.args.get('produto1')
    p2 = request.args.get('produto2')
    
    # O prompt solicita uma estrutura específica com separadores
    prompt = f"""
    Compare o produto {p1} com o produto {p2}.
    Retorne a resposta EXATAMENTE neste formato:
    ---FICHA_A---
    (Dados técnicos do {p1}: Preço, Tela, Bateria, Câmera, Processador)
    ---FICHA_B---
    (Dados técnicos do {p2}: Preço, Tela, Bateria, Câmera, Processador)
    ---ANALISE---
    (Veredito geral e recomendação)
    """
    
    try:
        response = model.generate_content(prompt)
        conteudo = response.text
        
        # Separando o texto conforme os marcadores
        partes = conteudo.split('---')
        ficha_a = partes[1].replace('FICHA_A', '') if len(partes) > 1 else "Dados não encontrados."
        ficha_b = partes[3].replace('FICHA_B', '') if len(partes) > 3 else "Dados não encontrados."
        analise_final = partes[5].replace('ANALISE', '') if len(partes) > 5 else "Análise indisponível."
    except Exception:
        ficha_a = ficha_b = analise_final = "Erro ao processar dados."
    
    return render_template('resultado.html', p1=p1, p2=p2, ficha_a=ficha_a, ficha_b=ficha_b, analise=analise_final)
