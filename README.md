🛡️ Linux Hardening Audit Tool

A Python-based Linux security auditing and hardening tool that performs baseline security checks, applies safe auto-fixes, and generates HTML and PDF audit reports.

This project is suitable for:

Academic mini / major projects

Cybersecurity demonstrations

Linux hardening practice

---

📁 Project Structure

linux-audit-tool/

├── auditor.py                  # Main entry point

├── checks/                     # Security check modules

├── fixer/                      # Safe auto-fix logic

├── report/                     # Generated reports (HTML & PDF)

├── generate_html_report.py     # HTML report generator

└── generate_pdf_report.py      # PDF report generator (ReportLab)

---

⚙️ Requirements

Python 3.8 or higher

Linux OS (Kali / Ubuntu / Debian recommended)

Root privileges (for some checks)

---

🐍 Python Virtual Environment (Recommended)

> Yes, ReportLab should be installed inside a virtual environment (venv)



This avoids system-level conflicts and keeps the project clean.

1️⃣ Create a virtual environment

    python3 -m venv venv

2️⃣ Activate the virtual environment

    source venv/bin/activate

You should now see:

(venv) user@linux-audit-tool$

---

📦 Install Required Python Packages

Install ReportLab (for PDF generation)

     pip install reportlab

reportlab → PDF report generation

---

▶️ Running the Tool

From the project root directory:

    sudo python3 auditor.py

> ⚠️ sudo is required for certain system-level security checks.

---

🖥️ Terminal Output (What the Tool Displays)

Audit progress

Passed / Failed checks

Hardening score

Safe auto-fix status

Verification results

Report generation status


Example outputs:

[+] Initial audit completed

[+] Failed checks: 1

[+] Hardening Score: 93/100

[!] Applying SAFE auto-fixes only

[+] Auto-fix completed

[+] HTML report generated: report/audit_report.html

[+] PDF report generated : report/audit_report.pdf


---

📄 Generated Reports

After execution, reports are saved in the report/ directory:

📄 HTML Report → report/audit_report.html

      firefox report/audit_report.html

  or

    xdg-open report/audit_report.html

📕 PDF Report  → report/audit_report.pdf

    firefox report/audit_report.pdf

or

    xdg-open report/audit_report.pdf
    
Both reports contain:

Audit summary

Individual security checks

Risk levels

Scores

Auto-fix information

---

🔓 Exiting the Virtual Environment

After finishing the project run, exit the venv using:

    deactivate

Your terminal will return to the normal system environment.

---

🔐 Auto-Fix Policy

✔ Safe fixes are applied automatically

❌ Critical or risky fixes are NOT auto-applied

🔁 Re-audit verifies applied fixes

This design follows real-world security best practices.

---
