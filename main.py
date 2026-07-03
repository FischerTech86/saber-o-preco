import os
import google.generativeai as genai
from flask import Flask, render_template, request

# Configuração da IA
genai.configure(api_key='SUA_CHAVE_AQUI')
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analise = None
    prod_a = request.form.get('prod_a')
    prod_b = request.form.get('prod_b')

    if prod_a and prod_b:
        # Pergunta para a IA
        prompt = f"Compare os produtos '{prod_a}' e '{prod_b}' de forma técnica, objetiva e profissional. Diga qual é a melhor escolha e por quê."
        response = model.generate_content(prompt)
        # Formata o texto para manter quebras de linha no HTML
        analise = response.text.replace('\n', '<br>')

    return render_template('index.html', analise=analise)

if __name__ == '__main__':
    app.run(debug=True)
