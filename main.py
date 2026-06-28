from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    termo = ""
    if request.method == 'POST':
        termo = request.form.get('query', '').strip()
    
    return render_template('index.html', termo=termo)

if __name__ == '__main__':
    app.run(debug=True)
