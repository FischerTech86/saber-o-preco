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
    
    # Leitura forçada da variável de ambiente no momento da consulta
    api_key = os.environ.get("GOOGLE_API_KEY")
    
    if not api_key:
        return "ERRO: A variável GOOGLE_API_KEY não foi encontrada. Verifique no Render se você escreveu exatamente 'GOOGLE_API_KEY' (tudo maiúsculo) na aba 'Environment'."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Liste 5 opções para o produto '{termo}'. Forneça: Nome, Preço Médio e Diferencial. Lista limpa."
        
        response = model.generate_content(prompt)
        lista_produtos = response.text
    except Exception as e:
        lista_produtos = f"Erro na comunicação com o Gemini: {str(e)}"

    return render_template('resultado.html', termo=termo, lista=lista_produtos)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
