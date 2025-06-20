from flask import Blueprint, send_file, current_app
import os
from fpdf import FPDF
import pandas as pd
from models.usuario_model import Usuario
from models.prestamo_model import Prestamo
from models.autores_model import Autores
from models.libro_model import Libro
from models.material_model import Material

reporte_bp = Blueprint('reporte', __name__, url_prefix='/reporte')  # <-- esto REINICIA todas las rutas


# ---------- EXCEL REPORTES ----------

@reporte_bp.route("/excel_prestamos")
def excel_prestamos():
    prestamos = Prestamo.get_all()
    df = pd.DataFrame([p.to_dict() for p in prestamos])
    path = os.path.join(current_app.root_path, 'static/reporte_prestamos.xlsx')
    df.to_excel(path, index=False)
    return send_file(path, as_attachment=True)

@reporte_bp.route("/excel_usuarios")
def excel_usuarios():
    usuarios = Usuario.get_all()
    df = pd.DataFrame([u.to_dict() for u in usuarios])
    path = os.path.join(current_app.root_path, 'static/reporte_usuarios.xlsx')
    df.to_excel(path, index=False)
    return send_file(path, as_attachment=True)

@reporte_bp.route("/excel_autores")
def excel_autores():
    autores = Autores.get_all()
    data = [{'id_autor': a.id_autor, 'nombre': a.nombre} for a in autores]
    df = pd.DataFrame(data)
    path = os.path.join(current_app.root_path, 'static/reporte_autores.xlsx')
    df.to_excel(path, index=False)
    return send_file(path, as_attachment=True)

@reporte_bp.route("/excel_libros")
def excel_libros():
    libros = Libro.get_all()
    df = pd.DataFrame([l.to_dict() for l in libros])
    path = os.path.join(current_app.root_path, 'static', 'reporte_libros.xlsx')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_excel(path, index=False)
    return send_file(path, as_attachment=True)
from models.material_model import Material

@reporte_bp.route("/excel_materiales")
def excel_materiales():
    materiales = Material.get_all()
    df = pd.DataFrame([m.to_dict() for m in materiales])
    path = os.path.join(current_app.root_path, "static", "reporte_materiales.xlsx")
    df.to_excel(path, index=False)
    return send_file(path, as_attachment=True)


# ---------- REPORTES PDF ----------

# ---------- CLASE BASE PDF CON LOGO Y DISEÑO ----------

class PDF(FPDF):
    def header(self):
        logo_path = os.path.join(current_app.root_path, 'static', 'logo.png')
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 8, 20)
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, self.titulo, 0, 1, "C")
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

def add_centered_table(pdf, headers, col_widths, data):
    table_width = sum(col_widths)
    start_x = (pdf.w - table_width) / 2
    pdf.set_x(start_x)
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, "C")
    pdf.ln()
    for row in data:
        pdf.set_x(start_x)
        for i, key in enumerate(row):
            pdf.cell(col_widths[i], 10, str(row.get(key, "")), 1, 0, "C")
        pdf.ln()



# ---------- REPORTES PDF ----------

@reporte_bp.route("/pdf_usuarios")
def pdf_usuarios():
    usuarios = Usuario.get_all()
    data = [u.to_dict() for u in usuarios]

    pdf = PDF()
    pdf.titulo = "Reporte de Usuarios"
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Definimos anchos de columna
    col_widths = [20, 60, 40]
    table_width = sum(col_widths)

    # Definimos posición X para centrar
    start_x = (pdf.w - table_width) / 2
    pdf.set_x(start_x)

    # Encabezado
    headers = ["ID", "Nombre", "Tipo"]
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, "C")
    pdf.ln()

    # Filas
    for row in data:
        pdf.set_x(start_x)  # posición inicial para cada fila
        pdf.cell(col_widths[0], 10, str(row["id"]), 1, 0, "C")
        pdf.cell(col_widths[1], 10, row["nombre"], 1, 0, "C")
        pdf.cell(col_widths[2], 10, row["tipo"], 1, 0, "C")
        pdf.ln()

    path = os.path.join(current_app.root_path, "static", "reporte_usuarios.pdf")
    pdf.output(path)
    return send_file(path, as_attachment=True)


@reporte_bp.route("/pdf_autores")
def pdf_autores():
    autores = Autores.get_all()
    data = [{'id_autor': a.id_autor, 'nombre': a.nombre} for a in autores]
    pdf = PDF()
    pdf.titulo = "Reporte de Autores"
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.cell(30, 10, "ID Autor", 1)
    pdf.cell(100, 10, "Nombre", 1)
    pdf.ln()
    for row in data:
        pdf.cell(30, 10, str(row['id_autor']), 1)
        pdf.cell(100, 10, row['nombre'], 1)
        pdf.ln()
    path = os.path.join(current_app.root_path, 'static', 'reporte_autores.pdf')
    pdf.output(path)
    return send_file(path, as_attachment=True)

@reporte_bp.route("/pdf_prestamos")
def pdf_prestamos():
    prestamos = Prestamo.get_all()
    data = [p.to_dict() for p in prestamos]

    pdf = PDF()
    pdf.titulo = "Reporte de Préstamos"
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Cabeceras
    pdf.cell(20, 10, "ID", 1)
    pdf.cell(40, 10, "Usuario", 1)
    pdf.cell(50, 10, "Material", 1)
    pdf.cell(40, 10, "Fecha Préstamo", 1)
    pdf.ln()

    # Contenido
    for row in data:
        pdf.cell(20, 10, str(row['id_prestamo']), 1)
        pdf.cell(40, 10, row['usuario'], 1)
        pdf.cell(50, 10, row['material'], 1)
        pdf.cell(40, 10, row['fecha_prestamo'], 1)  # Aquí usas la clave correcta
        pdf.ln()


    # Guardar y enviar el archivo
    path = os.path.join(current_app.root_path, 'static', 'reporte_prestamos.pdf')
    pdf.output(path)
    return send_file(path, as_attachment=True)

@reporte_bp.route("/pdf_libros")
def pdf_libros():
    libros = Libro.get_all()
    data = [l.to_dict() for l in libros]
    pdf = PDF()
    pdf.titulo = "Reporte de Libros"
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Cabecera
    pdf.cell(20, 10, "ID", 1)
    pdf.cell(30, 10, "ISBN", 1)
    pdf.cell(30, 10, "Material", 1)
    pdf.cell(40, 10, "Editorial", 1)
    pdf.cell(30, 10, "Año", 1)
    pdf.ln()

    for row in data:
        pdf.cell(20, 10, str(row['id_libro']), 1)
        pdf.cell(30, 10, str(row['isbn']), 1)
        pdf.cell(30, 10, row['material'], 1)      # Aquí usas el nombre en string
        pdf.cell(40, 10, row['editorial'], 1)    # Aquí también nombre en string
        pdf.cell(30, 10, str(row['anio_publicacion']), 1)
        pdf.ln()

    path = os.path.join(current_app.root_path, 'static', 'reporte_libros.pdf')
    pdf.output(path)
    return send_file(path, as_attachment=True)


@reporte_bp.route("/pdf_materiales")
def pdf_materiales():
    materiales = Material.get_all()
    data = [m.to_dict() for m in materiales]
    pdf = PDF()
    pdf.titulo = "Reporte de Materiales"
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.cell(20, 10, "ID", 1)
    pdf.cell(40, 10, "Tipo", 1)
    pdf.cell(50, 10, "Título", 1)
    pdf.cell(40, 10, "Categoría", 1)
    pdf.cell(40, 10, "Autor", 1)
    pdf.ln()
    for row in data:
        pdf.cell(20, 10, str(row['id_material']), 1)
        pdf.cell(40, 10, row['tipo'], 1)
        pdf.cell(50, 10, row['titulo'], 1)
        pdf.cell(40, 10, row['categoria'], 1)
        pdf.cell(40, 10, row['autor'], 1)
        pdf.ln()
    path = os.path.join(current_app.root_path, 'static', 'reporte_materiales.pdf')
    pdf.output(path)
    return send_file(path, as_attachment=True)
