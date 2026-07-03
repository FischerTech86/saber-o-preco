import os
import google.generativeai as genai
from flask import Flask, render_template, request

# IMPORTANTE: Coloque sua chave real aqui. Sem ela, nada funciona.
genai.configure(api_key='SUA_CHAVE_AQUI')
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analise = None
    erro = None
    prod_a = request.form.get('prod_a')
    prod_b = request.form.get('prod_b')

    if request.method == 'POST':
        if prod_a and prod_b:
            try:
                prompt = f"Compare os produtos '{prod_a}' e '{prod_b}' de forma técnica, objetiva e profissional. Destaque especificações e qual a melhor escolha."
                response = model.generate_content(prompt)
                analise = response.text.replace('\n', '<br>')
            except Exception as e:
                # Isso vai mostrar o erro no log do seu site para você saber o que está errado
                print(f"ERRO NA API: {e}")
                erro = f"Erro na IA: {e}" 

    return render_template('index.html', analise=analise, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
