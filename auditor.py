#!/usr/bin/env python3
import os
from checks.ssh import audit_ssh
from checks.firewall import audit_firewall
from checks.permissions import audit_permissions
from checks.system import audit_system
from fixer.ssh_fix import fix_ssh
from fixer.firewall_fix import fix_firewall
from checks.password_policy import audit_password_policy
from report_generator.html_report import generate_html_report
from report_generator.pdf_report import generate_pdf_report

results = []

def is_root():
    return os.geteuid() == 0

def add_result(name, status, fixable):
    if "PASS" in status:
        score = 0
        risk = "Low"
    elif fixable:
        score = 3
        risk = "Medium"
    else:
        score = 5
        risk = "High"

    results.append({
        "name": name,
        "status": status,
        "fixable": fixable,
        "score": score,
        "risk": risk
    })
def run_audit():
    add_result("SSH Hardening", audit_ssh(), True)
    add_result("Firewall Configuration", audit_firewall(), True)
    add_result("Critical File Permissions", audit_permissions(), False)
    add_result("ASLR Protection", audit_system(), False)

def apply_fixes():
    fix_ssh()
    fix_firewall()

if __name__ == "__main__":
    if not is_root():
        print("❌ Run as root (sudo python3 auditor.py)")
        exit(1)

    run_audit()

    print("📄 HTML report generated: report/audit_report.html")

    choice = input("Apply SAFE auto-fixes? (y/n): ").lower()
    if choice == "y":
        apply_fixes()
        print("✅ Auto-fixes applied safely")

def print_tool_report(results):
    print("\n=== LINUX HARDENING AUDIT TOOL REPORT ===\n")
    for r in results:
        print(f"[{r['risk']}] {r['name']}")
        print(f"  Status  : {r['status']}")
        print(f"  Score   : {r['score']}")
        print(f"  Fixable : {'Yes' if r['fixable'] else 'Manual'}\n")

    total = sum(r["score"] for r in results)
    print(f"TOTAL RISK SCORE: {total}")
    print("=======================================\n")
add_result("Password Policy", audit_password_policy(), False)
def print_terminal_output(results, score_before, score_after):
    total_checks = len(results)
    failed = sum(1 for r in results if r["status"] == "FAIL")
    passed = total_checks - failed
    fixed = sum(1 for r in results if r.get("fixed") is True)

    print("\n" + "=" * 50)
    print("        LINUX HARDENING AUDIT TOOL")
    print("=" * 50)

    print("\n[+] Audit completed")
    print(f"[+] Total checks      : {total_checks}")
    print(f"[+] Passed checks     : {passed}")
    print(f"[+] Failed checks     : {failed}")
    print(f"[+] Hardening score   : {score_before}/100")

    print("\n[+] Auto-fix execution summary")
    print(f"[+] Safe fixes applied: {fixed}")
    print("[!] Critical issues   : Manual fix required")

    print("\n[+] Report generation")
    print("[+] HTML report saved : report/audit_report.html")
    print("[+] PDF report saved  : report/audit_report.pdf")

    print(f"\n[+] Final score       : {score_after}/100")
    print("[+] Audit process completed successfully")
    print("=" * 50 + "\n")
# run checks → fill results list
score_before = 100 - sum(r["score"] for r in results)

# apply safe fixes here (if any)
score_after = 100 - sum(r["score"] for r in results if not r.get("fixed"))

generate_html_report(results)
generate_pdf_report(results)

print_terminal_output(results, score_before, score_after)
