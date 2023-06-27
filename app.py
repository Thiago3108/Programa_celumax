from flask import Flask
from flask import render_template, request, redirect

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("sitio/index.html")

@app.route("/admin/recibos")
def recibos():
    return render_template("admin/lrecibos.html")

@app.route("/productos")
def productos():
    return render_template("sitio/nproductos.html")

@app.route("/admin/adm")
def adm():
    return render_template("admin/oadmin.html")

@app.route("/admin")
def admin_index():
    return render_template("admin/index.html")

@app.route("/admin/login")
def admin_login():
    return render_template("admin/login.html")

@app.route("/admin/adm/guardar", methods=["POST"])
def admin_productos_guardar():
    _nombre=request.form["txtNombre"]
    _imagen=request.files["txtImagen"]
    _numero=request.form["txtNumber"]
    print(_nombre)
    print(_imagen)
    print(_numero)
    return redirect("/admin/adm")

if __name__ == "__main__":
    app.run(debug=True)