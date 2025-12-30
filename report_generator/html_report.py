import os
from datetime import datetime

def generate_html_report(results, output_dir="report"):
    """
    Generates a standalone HTML audit report.
    
    results: list of dicts with keys:
        - name: str
        - status: str
        - risk: str (Low/Medium/High)
        - score: int
        - fixable: bool
    """
    os.makedirs(output_dir, exist_ok=True)
    html_file = os.path.join(output_dir, "audit_report.html")

    total_score = sum(r.get("score", 0) for r in results)

    # Determine overall risk
    if total_score <= 4:
        overall = "LOW"
        color = "#22c55e"
    elif total_score <= 9:
        overall = "MEDIUM"
        color = "#facc15"
    else:
        overall = "HIGH"
        color = "#ef4444"

    html_content = f"""
    <html>
    <head>
        <title>Linux Hardening Audit Report</title>
        <style>
            body {{ background:#0f172a; color:#e5e7eb; font-family:Arial }}
            h1 {{ color:#38bdf8 }}
            table {{ width:100%; border-collapse:collapse; margin-top:20px }}
            th, td {{ padding:10px; border:1px solid #334155 }}
            th {{ background:#1e293b }}
            .Low {{ color:#22c55e }}
            .Medium {{ color:#facc15 }}
            .High {{ color:#ef4444 }}
        </style>
    </head>
    <body>
        <h1>Linux Hardening Audit Report</h1>
        <p>Generated on: {datetime.now()}</p>
        <h2>Overall Risk: <span style="color:{color}">{overall}</span> (Score: {total_score})</h2>
        <table>
            <tr>
                <th>Check</th>
                <th>Status</th>
                <th>Risk</th>
                <th>Score</th>
                <th>Auto Fix</th>
            </tr>
    """

    for r in results:
        fixable = "Yes" if r.get("fixable", False) else "Manual"
        html_content += f"""
            <tr>
                <td>{r.get('name', 'Unknown')}</td>
                <td>{r.get('status', 'UNKNOWN')}</td>
                <td class="{r.get('risk','Low')}">{r.get('risk','Low')}</td>
                <td>{r.get('score', 0)}</td>
                <td>{fixable}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(html_file, "w") as f:
        f.write(html_content)

    print(f"📄 HTML report generated: {html_file}")
