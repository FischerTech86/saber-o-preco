import os
import google.generativeai as genai
from flask import Flask, render_template, request

# Segurança: Substitua pela sua chave ou use variável de ambiente
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
            prompt = f"Compare os produtos '{prod_a}' e '{prod_b}' de forma técnica, objetiva e profissional. Diga qual é a melhor escolha e por quê."
            response = model.generate_content(prompt)
            analise = response.text.replace('\n', '<br>')
        except Exception:
            erro = "Desculpe, não foi possível realizar a análise no momento. Tente novamente."

    return render_template('index.html', analise=analise, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
