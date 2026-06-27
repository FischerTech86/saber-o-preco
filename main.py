from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Simulação simples de banco de dados para os produtos
def buscar_dados_produto(nome):
    # Aqui é onde, no futuro, você usará a API da IA para buscar dados reais
    return {
        "nome": nome.upper(),
        "tela": "6.7 polegadas AMOLED",
        "bateria": "5000 mAh",
        "processador": "Octa-core de alta performance",
        "camera": "108 MP"
    }

@app.route('/ia', methods=['GET', 'POST'])
def ia():
    res_a = None
    res_b = None
    analise = None

    if request.method == 'POST':
        prod_a = request.form.get('prodA')
        prod_b = request.form.get('prodB')
        
        # Busca os dados (Simulando)
        res_a = buscar_dados_produto(prod_a)
        res_b = buscar_dados_produto(prod_b)
        
        # Aqui a IA diria o veredito
        analise = f"Análise: O {res_a['nome']} se destaca pelo processamento, enquanto o {res_b['nome']} oferece um melhor custo-benefício em tela. Recomendamos o {res_a['nome']} para uso intenso."

    return render_template('ia.html', res_a=res_a, res_b=res_b, analise=analise)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
