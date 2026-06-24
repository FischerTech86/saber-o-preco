from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

# Configuração da chave de API
api_key = os.environ.get("GOOGLE_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    termo = request.args.get('pesquisa', 'Produto')
    
    if not api_key:
        return "ERRO GRAVE: A variável GOOGLE_API_KEY não foi encontrada pelo servidor. Verifique a aba 'Environment' no Render."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Liste 5 opções, marcas ou modelos para o produto '{termo}'. Para cada um, forneça: Nome do Produto, Preço Médio Estimado e um Curto Diferencial. Formate como uma lista limpa."
        
        response = model.generate_content(prompt)
        lista_produtos = response.text
    except Exception as e:
        lista_produtos = f"Erro ao processar busca: {str(e)}"

    return render_template('resultado.html', termo=termo, lista=lista_produtos)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
