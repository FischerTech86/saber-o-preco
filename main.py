from flask import Flask, render_template, request
import os
import time
import google.generativeai as genai

app = Flask(__name__)

# Configuração da chave de API
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    termo = request.args.get('pesquisa', 'Produto')
    
    prompt = f"""
    Liste 5 opções, marcas ou modelos para o produto '{termo}'.
    Para cada um, forneça: Nome do Produto, Preço Médio Estimado e um Curto Diferencial.
    Formate como uma lista limpa, sem introduções longas.
    """
    
    lista_produtos = None
    
    # SISTEMA DE PROTEÇÃO: Tenta até 3 vezes antes de dar erro
    for tentativa in range(3):
        try:
            response = model.generate_content(
                prompt,
                # Desativa filtros de segurança para evitar falsos positivos
                safety_settings={
                    'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
                    'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
                    'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
                    'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE'
                }
            )
            lista_produtos = response.text
            break  # Se a resposta der certo, quebra o loop e segue o jogo
        except Exception as e:
            print(f"Tentativa {tentativa + 1} falhou: {e}")
            time.sleep(2)  # Espera 2 segundos antes da próxima tentativa
            
    # FALLBACK DE EMERGÊNCIA: Se as 3 tentativas falharem
    if not lista_produtos:
        lista_produtos = "Nossos servidores estão muito ocupados processando outras buscas no momento.\n\nPor favor, aguarde alguns segundos e clique em Nova Busca."
        
    return render_template('resultado.html', termo=termo, lista=lista_produtos)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
