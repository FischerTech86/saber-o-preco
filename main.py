from flask import Flask, render_template, request
import os
import google.generativeai as genai
from config import Config

# Validação obrigatória da chave
Config.validate()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    termo = request.args.get('pesquisa', 'Produto')
    
    try:
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Prompt otimizado para o Python separar os dados depois
        prompt = f"Liste 5 opções para o produto '{termo}'. Formate cada linha exatamente assim: Nome do Produto;Preço Médio;Diferencial. Não escreva introduções."
        
        response = model.generate_content(prompt)
        
        # Processamento: transforma o texto em uma lista de objetos
        lista_final = []
        linhas = response.text.strip().split('\n')
        
        for linha in linhas:
            if ';' in linha:
                partes = linha.split(';')
                if len(partes) >= 3:
                    nome = partes[0].strip()
                    preco = partes[1].strip()
                    dif = partes[2].strip()
                    # Link mágico para o Google Shopping
                    link = f"https://www.google.com/search?q={nome.replace(' ', '+')}&tbm=shop"
                    lista_final.append({'nome': nome, 'preco': preco, 'dif': dif, 'link': link})
        
        # Caso o Gemini não siga o formato, envia o texto bruto
        if not lista_final:
            lista_final = [{'nome': "Erro na formatação", 'preco': "-", 'dif': response.text, 'link': "#"}]

    except Exception as e:
        lista_final = [{'nome': "Erro", 'preco': "-", 'dif': str(e), 'link': "#"}]

    return render_template('resultado.html', termo=termo, lista=lista_final)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
