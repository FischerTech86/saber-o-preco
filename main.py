from flask import Flask, render_template, request
import os

app = Flask(__name__)

def gerar_analise_inteligente(pA, pB):
    # Transformamos tudo em minúsculo para facilitar a comparação
    a = pA.lower()
    b = pB.lower()
    
    # Lógica de "IA" Simulada (Heurística)
    if "iphone" in a or "iphone" in b:
        if "samsung" in a or "samsung" in b:
            return "Análise: Comparativo de gigantes. O iPhone foca no ecossistema fechado (iOS) e valor de revenda, enquanto os dispositivos Samsung (Android) oferecem maior liberdade de customização, telas superiores e multitarefa avançada. A escolha depende da sua preferência de sistema operacional."
    
    if "arroz" in a or "arroz" in b:
        return "Análise: Comparativo de custo-benefício. Verifique sempre o peso líquido (kg) e a classificação do tipo (Tipo 1 é o mais selecionado). Produtos de marcas líderes geralmente oferecem grãos mais inteiros, enquanto marcas de entrada são ideais para o dia a dia doméstico."
    
    # Caso genérico para qualquer outro produto
    return f"Análise: Comparando '{pA}' e '{pB}'. Para decidir entre eles, considere: 1) O custo de manutenção a longo prazo; 2) A finalidade de uso (profissional vs casual); 3) Avaliações de outros usuários. Recomendamos focar na durabilidade se o produto for de uso diário."

@app.route('/', methods=['GET', 'POST'])
def index():
    termo = request.args.get('pesquisa', '')
    lista_busca = []
    
    # Variáveis para a Comparação
    analise = None
    prodA = None
    prodB = None

    # Lógica da Busca
    if termo:
        busca_url = termo.replace(" ", "+")
        lista_busca = [{'nome': f'{termo} Premium', 'link': '#'}, {'nome': f'{termo} Padrão', 'link': '#'}]

    # Lógica da IA (Agora melhorada!)
    if request.method == 'POST':
        prodA = request.form.get('prodA')
        prodB = request.form.get('prodB')
        if prodA and prodB:
            analise = gerar_analise_inteligente(prodA, prodB)

    return render_template('index.html', lista=lista_busca, analise=analise, prodA=prodA, prodB=prodB)

@app.route('/dicas')
def dicas(): return render_template('dicas.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

