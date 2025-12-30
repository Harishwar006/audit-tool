def audit_ssh():
    try:
        with open("/etc/ssh/sshd_config") as f:
            data = f.read()
        if "PermitRootLogin no" in data and "PasswordAuthentication no" in data:
            return "PASS"
        return "FAIL"
    except:
        return "NOT INSTALLED"
