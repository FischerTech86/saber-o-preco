from flask import Flask, render_template, request
import os
import time
import google.generativeai as genai
from config import Config  # <--- ESSA LINHA CONECTA OS DOIS ARQUIVOS

# Validar configuração logo no início
Config.validate()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    termo = request.args.get('pesquisa', 'Produto')
    
    # Agora usamos a chave que vem do config.py
    api_key = Config.GOOGLE_API_KEY

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Liste 5 opções para o produto '{termo}'. Forneça: Nome, Preço Médio e Diferencial. Lista limpa."
        
        response = model.generate_content(prompt)
        lista_produtos = response.text
    except Exception as e:
        lista_produtos = f"Erro na conexão com a IA: {str(e)}"

    return render_template('resultado.html', termo=termo, lista=lista_produtos)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
