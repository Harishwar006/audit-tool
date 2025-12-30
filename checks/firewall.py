import subprocess

def audit_firewall():
    result = subprocess.getoutput("ufw status")
    return "PASS" if "Status: active" in result else "FAIL"
