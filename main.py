from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    termo = request.args.get('pesquisa', 'Produto')
    api_key = os.environ.get("GOOGLE_API_KEY")

    # Se não tiver chave, o site não trava, apenas avisa na tela
    if not api_key:
        mensagem = "A chave da API não está configurada no servidor. Por favor, adicione a variável GOOGLE_API_KEY no Render."
        return render_template('resultado.html', termo=termo, lista=mensagem)

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Liste 5 opções para o produto '{termo}'. Formate como: Nome;Preço;Diferencial."
        response = model.generate_content(prompt)
        
        resultado_final = response.text 
    except Exception as e:
        resultado_final = f"Ocorreu um erro ao processar: {str(e)}"

    return render_template('resultado.html', termo=termo, lista=resultado_final)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
