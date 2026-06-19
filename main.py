import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        produto = request.form.get('produto', '').strip()
        if produto:
            # Redireciona para o Google Shopping diretamente
            return redirect(f"https://www.google.com/search?q={produto}&tbm=shop")
    
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
