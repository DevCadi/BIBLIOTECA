from flask import Blueprint, send_file
import pandas as pd
from fpdf import FPDF
from models.usuario_model import Usuario
from models.prestamo_model import Prestamo
import os
from flask import current_app

reporte_bp = Blueprint('reporte', __name__, url_prefix='/reporte')

@reporte_bp.route("/excel_prestamos")
def excel_prestamos():
    prestamos = Prestamo.get_all() 
    df = pd.DataFrame([p.to_dict() for p in prestamos])
    path = "static/reporte_prestamos.xlsx"
    df.to_excel(path, index=False)
    return send_file(path, as_attachment=True)

@reporte_bp.route("/excel_usuarios")
def excel_usuarios():
    usuarios = Usuario.get_all()
    df = pd.DataFrame([u.to_dict() for u in usuarios])
    path = "static/reporte_usuarios.xlsx"
    df.to_excel(path, index=False)
    return send_file(path, as_attachment=True)


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

    # Asegurar que la carpeta 'static' exista
    output_folder = os.path.join(current_app.root_path, 'static')
    os.makedirs(output_folder, exist_ok=True)

    # Ruta absoluta del archivo
    output_path = os.path.join(output_folder, "reporte_usuarios.pdf")
    pdf.output(output_path)

    return send_file(output_path, as_attachment=True)
