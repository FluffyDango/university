from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, Frame, PageTemplate, BaseDocTemplate
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib import utils
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf(queries: list, output: str) -> None:
    """Generate PDF file from queries"""

    doc = BaseDocTemplate(output, pagesize=letter)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    # Create styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    # Create table
    data = []
    table_columns = {'FN': 'Name', 'TEL': 'Phone', 'EMAIL': 'Email', 'ORG': 'Organization', 'TITLE': 'Title', 'URL': 'URL'}
    # Append every table column key to data
    data.append([table_columns[key] for key in table_columns])
    # Append every query to data
    for query in queries:
        data_list = []
        for key, value in table_columns.items():
            data_list.append(query.get(key))
        data.append(data_list)

    table = Table(data, colWidths=1.3*inch)
    # Add table style
    table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                               ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                               ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black)]))
    # Add table to canvas
    elements = []
    elements.append(table)
    doc.addPageTemplates([PageTemplate(id='AllPages', frames=frame)])
    doc.build(elements)