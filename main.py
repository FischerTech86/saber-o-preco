import os
import google.generativeai as genai
from flask import Flask, render_template, request

# Substitua 'SUA_CHAVE_AQUI' pela sua chave da API
genai.configure(api_key='SUA_CHAVE_AQUI')
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analise = None
    erro = None
    prod_a = request.form.get('prod_a')
    prod_b = request.form.get('prod_b')

    if prod_a and prod_b:
        try:
            # Prompt focado em resposta técnica e explicativa
            prompt = f"Compare os produtos '{prod_a}' e '{prod_b}' de forma técnica, objetiva e profissional. Destaque especificações, desempenho e dê um veredito técnico sobre qual é a melhor escolha."
            response = model.generate_content(prompt)
            analise = response.text.replace('\n', '<br>')
        except Exception:
            erro = "Erro ao gerar análise. Tente novamente."

    return render_template('index.html', analise=analise, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
