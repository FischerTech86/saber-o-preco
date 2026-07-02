from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    termo = None
    if request.method == 'POST':
        termo = request.form.get('query')
    return render_template('index.html', termo=termo)

if __name__ == '__main__':
    app.run(debug=True)
