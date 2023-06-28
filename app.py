from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL

app=Flask(__name__)
mysql=MySQL()


app.config["MYSQL_DATABASE_HOST"]="localhost"   #dominio, localhost, entre otros 
app.config["MYSQL_DATABASE_USER"]="root"
app.config["MYSQL_DATABASE_PASSWORD"]=""
app.config["MYSQL_DATABASE_DB"]="sitio"
mysql.init_app(app)


@app.route("/")
def inicio():
    return render_template("sitio/index.html")

@app.route("/admin/recibos")
def recibos():
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `recibos`")
    recibos=cursor.fetchall()
    conexion.commit()
    print(recibos)

    return render_template("admin/lrecibos.html", recibos=recibos)

@app.route("/productos")
def productos():
    return render_template("sitio/nproductos.html")

@app.route("/admin/adm")
def adm():
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `productos`")
    productos=cursor.fetchall()
    conexion.commit()
    print(productos)

    return render_template("admin/oadmin.html", productos=productos)

@app.route("/admin")
def admin_index():
    return render_template("admin/index.html")

@app.route("/admin/login")
def admin_login():
    return render_template("admin/login.html")

@app.route("/admin/adm/guardar", methods=["POST"])
def admin_producto_guardar():
    _producto=request.form["txtProducto"]
    _img=request.files["txtImagen"]
    _precio=request.form["txtPrecio"]
    _no=request.form["txtNumber"]

    sql="INSERT INTO `productos` (`ID`, `Producto`, `Imagen`, `Precio`, `No`) VALUES (NULL,%s, %s, %s,%s);"
    datos2=(_producto,_img,_precio,_no)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos2)
    conexion.commit()

    print(_producto)
    print(_img)
    print(_precio)
    print(_no)

    return redirect("/admin/adm")

@app.route("/admin/adm/borrar", methods=["POST"])
def admin_producto_borrar():

    _id2=request.form["txtID2"]
    print(_id2)

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `productos` WHERE id=%s",(_id2))
    productos=cursor.fetchall()
    conexion.commit()
    print(productos)

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id=%s",(_id2))
    conexion.commit()

    return redirect("/admin/adm")


@app.route("/admin/recibos/guardar", methods=["POST"])
def admin_recibos_guardar():
    _nombre=request.form["txtNombrerecibo"]
    _cc=request.form["txtCC"]
    _tel=request.form["txtTel"]
    _equipo=request.form["txtEquipo"]
    _imei=request.form["txtImei"]
    _procedimiento=request.form["txtProcedimiento"]
    _valor=request.form["txtValor"]
    _abono=request.form["txtAbono"]
    _clave=request.form["txtClave"]


    sql="INSERT INTO `recibos` (`ID`, `Fecha`, `Nombre`, `CC.`, `Tel.`, `Equipo`, `Imei`, `Procedimiento`, `Valor`, `Abono`, `Clave`) VALUES (NULL, current_timestamp(), %s, %s, %s,%s,%s, %s, %s, %s, %s);"
    datos=(_nombre,_cc,_tel,_equipo,_imei,_procedimiento,_valor,_abono,_clave)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

    print(_nombre)
    print(_cc)
    print(_tel)
    print(_equipo)
    print(_imei)
    print(_procedimiento)
    print(_valor)
    print(_abono)
    print(_clave)
    return redirect("/admin/recibos")

@app.route("/admin/recibos/borrar", methods=["POST"])
def admin_recibo_borrar():

    _id=request.form["txtID"]
    print(_id)

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `recibos` WHERE id=%s",(_id))
    recibos=cursor.fetchall()
    conexion.commit()
    print(recibos)

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM recibos WHERE id=%s",(_id))
    conexion.commit()

    return redirect("/admin/recibos")

if __name__ == "__main__":
    app.run(debug=True)