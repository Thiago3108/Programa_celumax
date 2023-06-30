@app.route("/admin/recibos/imprimir", methods=["POST"])
def admin_recibo_imprimir():
    if not "login" in session:
        return redirect("/admin/login")

    _nombre = request.form["txtNombrerecibo"]
    _cc = request.form["txtCC"]
    _tel = request.form["txtTel"]
    _equipo = request.form["txtEquipo"]
    _imei = request.form["txtImei"]
    _procedimiento = request.form["txtProcedimiento"]
    _valor = request.form["txtValor"]
    _abono = request.form["txtAbono"]
    _clave = request.form["txtClave"]

    datos = {
        "Nombre": _nombre,
        "CC": _cc,
        "Tel": _tel,
        "Equipo": _equipo,
        "Imei": _imei,
        "Procedimiento": _procedimiento,
        "Valor": _valor,
        "Abono": _abono,
        "Clave": _clave
    }

    # Construir la ruta al documento existente
    ruta_documento = os.path.join(current_app.root_path, "templates", "sitio", "recibos", "Recibos.docx")

    # Abrir el documento existente
    document = Document(ruta_documento)

    # Obtener el cuerpo principal del documento
    cuerpo_principal = document.paragraphs

    # Acceder al último párrafo existente
    ultimo_parrafo = cuerpo_principal[11]
    ultimo_parrafo.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    ultimo_parrafo.space_after = Pt(12)

    # Añadir los inputs al último párrafo
    for campo, valor in datos.items():
        run = ultimo_parrafo.add_run(f"{campo}: {valor}\n")
        run.bold = True  # Opcional: establecer el texto en negrita
        run.font.size = Pt(9)

    # Guardar el documento modificado
    ruta_documento_modificado = os.path.join(current_app.root_path, "templates", "sitio", "recibos", "Recibos", f"{_nombre}.docx")
    document.save(ruta_documento_modificado)

    # Imprimir el documento
    win32api.ShellExecute(0, "print", ruta_documento_modificado, None, ".", 0)

    return redirect("/admin/recibos")