import os
import google.generativeai as genai
from flask import Flask, render_template, request

# Cole sua chave aqui dentro das aspas, mantendo as aspas
API_KEY = 'SUA_CHAVE_AQUI'

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analise = None
    if request.method == 'POST':
        prod_a = request.form.get('prod_a')
        prod_b = request.form.get('prod_b')
        if prod_a and prod_b:
            try:
                prompt = f"Compare os produtos '{prod_a}' e '{prod_b}' de forma técnica e objetiva."
                response = model.generate_content(prompt)
                analise = response.text.replace('\n', '<br>')
            except:
                analise = "Erro na conexão com a IA. Verifique se a API KEY está correta."
    return render_template('index.html', analise=analise)

if __name__ == '__main__':
    app.run()
