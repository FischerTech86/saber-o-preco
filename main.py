from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    link = None
    termo = None
    if request.method == "POST":
        termo = request.form.get("produto")
        if termo:
            termo_formatado = termo.replace(" ", "%20")
            link = "https://lista.mercadolivre.com.br/" + termo_formatado
    return render_template("index.html", link=link, termo=termo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
