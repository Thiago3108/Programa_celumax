from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("sitio/index.html")

@app.route("/recibos")
def recibos():
    return render_template("sitio/lrecibos.html")

@app.route("/productos")
def productos():
    return render_template("sitio/nproductos.html")

if __name__ == "__main__":
    app.run(debug=True)