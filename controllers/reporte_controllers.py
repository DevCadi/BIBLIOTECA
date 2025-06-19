from flask import Blueprint, send_file, current_app
import pandas as pd
from fpdf import FPDF
from models.usuario_model import Usuario
from models.prestamo_model import Prestamo
from models.autores_model import Autores
from models.libro_model import Libro
import os

reporte_bp = Blueprint('reporte', __name__, url_prefix='/reporte')

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

# ---------- PDF REPORTES ----------

@reporte_bp.route("/pdf_usuarios")
def pdf_usuarios():
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, "Reporte de Usuarios", 0, 1, "C")

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

        def add_table(self, data):
            self.set_font("Arial", "", 12)
            for row in data:
                self.cell(10, 10, str(row['id']), 1)
                self.cell(50, 10, row['nombre'], 1)
                self.cell(40, 10, row['tipo'], 1)
                self.ln()

    usuarios = Usuario.get_all()
    pdf = PDF()
    pdf.add_page()
    pdf.add_table([u.to_dict() for u in usuarios])
    output_path = os.path.join(current_app.root_path, 'static/reporte_usuarios.pdf')
    pdf.output(output_path)
    return send_file(output_path, as_attachment=True)

@reporte_bp.route("/pdf_autores")
def pdf_autores():
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, "Reporte de Autores", 0, 1, "C")

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

        def add_table(self, data):
            self.set_font("Arial", "", 12)
            for row in data:
                self.cell(30, 10, str(row['id_autor']), 1)
                self.cell(100, 10, row['nombre'], 1)
                self.ln()

    autores = Autores.get_all()
    data = [{'id_autor': a.id_autor, 'nombre': a.nombre} for a in autores]
    pdf = PDF()
    pdf.add_page()
    pdf.add_table(data)
    output_path = os.path.join(current_app.root_path, 'static/reporte_autores.pdf')
    pdf.output(output_path)
    return send_file(output_path, as_attachment=True)

@reporte_bp.route("/pdf_prestamos")
def pdf_prestamos():
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, "Reporte de Préstamos", 0, 1, "C")

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

        def add_table(self, data):
            self.set_font("Arial", "", 10)
            for row in data:
                self.cell(20, 10, str(row.get('id_prestamo')), 1)
                self.cell(40, 10, str(row.get('usuario')), 1)
                self.cell(40, 10, str(row.get('material')), 1)
                self.cell(40, 10, str(row.get('fecha')), 1)
                self.ln()

    prestamos = Prestamo.get_all()
    data = [p.to_dict() for p in prestamos]
    pdf = PDF()
    pdf.add_page()
    pdf.add_table(data)
    output_path = os.path.join(current_app.root_path, 'static/reporte_prestamos.pdf')
    pdf.output(output_path)
    return send_file(output_path, as_attachment=True)

@reporte_bp.route("/pdf_libros")
def pdf_libros():
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, "Reporte de Libros", 0, 1, "C")

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

        def add_table(self, data):
            self.set_font("Arial", "", 10)
            self.cell(20, 10, "ID", 1)
            self.cell(40, 10, "ISBN", 1)
            self.cell(30, 10, "Material", 1)
            self.cell(30, 10, "Editorial", 1)
            self.cell(30, 10, "Año", 1)
            self.ln()

            for row in data:
                self.cell(20, 10, str(row['id_libro']), 1)
                self.cell(40, 10, str(row['isbn']), 1)
                self.cell(30, 10, str(row['id_material']), 1)
                self.cell(30, 10, str(row['id_editorial']), 1)
                self.cell(30, 10, row['anio_publicacion'], 1)
                self.ln()

    libros = Libro.get_all()
    pdf = PDF()
    pdf.add_page()
    pdf.add_table([l.to_dict() for l in libros])

    path = os.path.join(current_app.root_path, 'static', 'reporte_libros.pdf')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pdf.output(path)

    return send_file(path, as_attachment=True)