import os

def audit_permissions():
    try:
        passwd = oct(os.stat("/etc/passwd").st_mode & 0o777)
        shadow = oct(os.stat("/etc/shadow").st_mode & 0o777)

        if passwd == "0o644" and shadow in ["0o640", "0o600"]:
            return "PASS"
        return "FAIL"
    except:
        return "ERROR"
