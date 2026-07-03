from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analise = None
    prod_a = request.form.get('prod_a')
    prod_b = request.form.get('prod_b')

    # Lógica que gera a análise técnica quando os produtos são enviados
    if prod_a and prod_b:
        analise = (
            f"Análise Técnica: {prod_a} vs {prod_b}. "
            f"O {prod_a} possui uma arquitetura de processamento superior, otimizada para multitarefas pesadas e alta taxa de atualização. "
            f"Por outro lado, o {prod_b} se destaca em eficiência energética e qualidade de sensores fotográficos, sendo uma opção mais equilibrada para uso contínuo sem preocupação com recarga frequente. "
            "A escolha depende se você prioriza performance bruta ou longevidade de bateria."
        )

    return render_template('index.html', analise=analise, prod_a=prod_a, prod_b=prod_b)

if __name__ == '__main__':
    app.run(debug=True)
