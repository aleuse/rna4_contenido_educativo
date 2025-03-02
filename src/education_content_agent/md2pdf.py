import os
from datetime import datetime
import markdown
from xhtml2pdf import pisa

class DocumentConverter:
    def __init__(self, temp_dir="temp", output_dir="output"):
        """
        Inicializa el conversor de documentos.
        """
        self.temp_dir = temp_dir
        self.output_dir = output_dir
        self._crear_directorios()

    def _crear_directorios(self):
        """Crea los directorios necesarios si no existen."""
        os.makedirs(self.temp_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def read_results(self):
        """
        Lee y combina los archivos MD generados por los agentes.
        """
        archivos = {
            "Class Notes": "class_notes.md",
            "Learning Objectives": "learning_objectives.md",
            "Practice Problems": "practice_problems.md",
            "Discussion Questions": "discussion_questions.md",
            "Resource Recommendations": "resource_recommendation.md"
        }
        
        results = "# Contenido Educativo Generado\n\n"
        results += f"*Generado el {datetime.now().strftime('%d/%m/%Y %H:%M')}*\n\n"

        for titulo, archivo in archivos.items():
            ruta = os.path.join(self.temp_dir, archivo)
            try:
                with open(ruta, "r", encoding='utf-8') as file:
                    contenido = file.read().strip()
                results += f"\n## {titulo}\n\n{contenido}\n\n"
            except FileNotFoundError:
                print(f"⚠ Advertencia: No se encontró el archivo {archivo}")
                results += f"\n## {titulo}\n\n*Contenido no disponible*\n\n"
        
        return results

    def markdown_to_pdf(self, output_filename="resultado_final.pdf"):
        """
        Convierte el contenido Markdown combinado a PDF usando xhtml2pdf.
        """
        # Obtener el contenido Markdown
        markdown_content = self.read_results()
        
        # Convertir Markdown a HTML
        html_content = markdown.markdown(markdown_content)
        
        # Añadir estilos CSS
        html_with_style = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                @page {{
                    size: letter;
                    margin: 2cm;
                }}
                body {{
                    font-family: Arial, sans-serif;
                    font-size: 12px;
                    line-height: 1.6;
                }}
                h1 {{
                    color: #2c3e50;
                    font-size: 24px;
                    border-bottom: 2px solid #3498db;
                    margin-bottom: 20px;
                }}
                h2 {{
                    color: #34495e;
                    font-size: 18px;
                    margin-top: 30px;
                }}
                code {{
                    background: #f8f9fa;
                    padding: 2px 5px;
                    font-family: monospace;
                }}
                pre {{
                    background: #f8f9fa;
                    padding: 15px;
                    border-radius: 5px;
                    font-family: monospace;
                    white-space: pre-wrap;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Generar PDF
        output_path = os.path.join(self.output_dir, output_filename)
        
        # Crear el PDF usando xhtml2pdf
        with open(output_path, "w+b") as output_file:
            pisa_status = pisa.CreatePDF(
                html_with_style,
                dest=output_file,
                encoding='utf-8'
            )
        
        if pisa_status.err:
            print("❌ Error al generar el PDF")
            return None
            
        print(f"✅ PDF generado exitosamente: {output_path}")
        return output_path