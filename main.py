import google.generativeai as genai
from flask import Flask, render_template, request

# --- INSERIR CHAVE AQUI ---
# Substitua o texto abaixo pela sua chave real (ex: 'AIzaSy...')
API_KEY = 'SUA_CHAVE_AQUI' 
# --------------------------

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analise = None
    erro = None
    
    if request.method == 'POST':
        prod_a = request.form.get('prod_a')
        prod_b = request.form.get('prod_b')
        
        if prod_a and prod_b:
            try:
                prompt = f"Compare os produtos '{prod_a}' e '{prod_b}' de forma técnica, objetiva e profissional. Destaque especificações e qual a melhor escolha."
                response = model.generate_content(prompt)
                analise = response.text.replace('\n', '<br>')
            except Exception as e:
                erro = "Erro ao conectar com a IA. Verifique se a sua API KEY está correta no arquivo main.py."

    return render_template('index.html', analise=analise, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
