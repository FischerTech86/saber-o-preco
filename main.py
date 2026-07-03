from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Captura a busca ou a comparação
    termo = request.form.get('query') or request.form.get('prod_a')
    return render_template('index.html', termo=termo)

if __name__ == '__main__':
    app.run(debug=True)
