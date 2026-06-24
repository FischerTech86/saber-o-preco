from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)
# Certifique-se de que GOOGLE_API_KEY esteja no painel do Render
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    termo = request.args.get('pesquisa')
    # Prompt focado em listar produtos
    prompt = f"Liste 5 marcas ou modelos para o produto '{termo}' com Preço Médio Estimado e um Diferencial. Formate como uma lista simples."
    
    try:
        response = model.generate_content(prompt)
        lista_produtos = response.text
    except Exception:
        lista_produtos = "Erro ao buscar sugestões. Tente novamente."
        
    return render_template('resultado.html', termo=termo, lista=lista_produtos)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
