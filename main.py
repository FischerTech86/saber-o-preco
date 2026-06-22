from flask import Flask, render_template
import os

app = Flask(__name__)

# Mantenha suas rotas atuais para o site não mudar nada
@app.route('/resultado')
def resultado():
    # AQUI É ONDE VOCÊ ATUALIZA A IA
    # Você não precisa mudar o site, apenas o texto desta variável:
    nova_analise_da_ia = "Aqui vai a nova resposta da sua IA após a atualização..."
    
    return render_template('resultado.html', analise=nova_analise_da_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
