import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configuração segura: O código busca a chave do ambiente (Render)
# Se não estiver no Render, ele usa None para evitar travar
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'reply': 'Por favor, digite algo.'})
    
    try:
        response = model.generate_content(user_message)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'reply': 'Erro: Verifique se a API KEY está configurada corretamente no Render.'})

if __name__ == '__main__':
    app.run()
