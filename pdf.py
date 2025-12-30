from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_pdf_report(results):
    doc = SimpleDocTemplate("report/audit_report.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Linux Hardening Audit Report", styles["Title"]))

    data = [["Check", "Status", "Risk", "Score", "Fix"]]
    for r in results:
        data.append([
            r["name"],
            r["status"],
            r["risk"],
            str(r["score"]),
            "Auto" if r["fixable"] else "Manual"
        ])

    table = Table(data)
    table.setStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.grey),
        ("BACKGROUND", (0,0), (-1,0), colors.lightblue)
    ])

    elements.append(table)
    doc.build(elements)
