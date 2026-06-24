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
    
    # Pega a chave da API do servidor
    api_key = os.environ.get("GOOGLE_API_KEY")
    
    # Se a chave nem existir, ele já avisa na tela
    if not api_key:
         return render_template('resultado.html', termo=termo, lista="ERRO GRAVE: O Render não encontrou a sua GOOGLE_API_KEY. Você precisa adicionar ela na aba 'Environment' do Render.")

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Liste 3 opções de {termo} de forma bem curta."
        response = model.generate_content(prompt)
        
        lista_produtos = response.text
        
    except Exception as e:
        # AQUI ESTÁ A MÁGICA: Ele vai escrever na tela o erro exato que o Google ou o servidor retornar!
        lista_produtos = f"ERRO TÉCNICO DETECTADO:\n\n{str(e)}\n\n(Copie esse erro e mande para o assistente)"

    return render_template('resultado.html', termo=termo, lista=lista_produtos)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
