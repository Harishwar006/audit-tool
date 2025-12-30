import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_pdf_report(results, output_dir="report"):
    """
    Generates a standalone PDF audit report.
    
    results: list of dicts with keys:
        - name: str
        - status: str
        - risk: str (Low/Medium/High)
        - score: int
        - fixable: bool
    """
    os.makedirs(output_dir, exist_ok=True)
    pdf_file = os.path.join(output_dir, "audit_report.pdf")

    total_score = sum(r.get("score", 0) for r in results)

    # Determine overall risk
    if total_score <= 4:
        overall = "LOW"
        color = colors.green
    elif total_score <= 9:
        overall = "MEDIUM"
        color = colors.orange
    else:
        overall = "HIGH"
        color = colors.red

    doc = SimpleDocTemplate(pdf_file, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Linux Hardening Audit Report", styles["Title"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Generated on: {datetime.now()}", styles["Normal"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Overall Risk: {overall} (Score: {total_score})", styles["Heading2"]))
    elements.append(Spacer(1, 12))

    # Table header
    table_data = [["Check", "Status", "Risk", "Score", "Auto Fix"]]

    for r in results:
        fixable = "Yes" if r.get("fixable", False) else "Manual"
        table_data.append([
            r.get("name", "Unknown"),
            r.get("status", "UNKNOWN"),
            r.get("risk", "Low"),
            str(r.get("score", 0)),
            fixable
        ])

    table = Table(table_data, repeatRows=1)
    table.setStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("ALIGN", (3,1), (3,-1), "CENTER")
    ])

    elements.append(table)
    doc.build(elements)

    print(f"📄 PDF report generated: {pdf_file}")
