def audit_password_policy():
    try:
        with open("/etc/login.defs") as f:
            data = f.read()

        issues = []
        if "PASS_MIN_LEN" not in data:
            issues.append("No minimum password length")
        if "PASS_MAX_DAYS" not in data:
            issues.append("Password expiry not set")

        return "PASS" if not issues else "FAIL (Manual Fix Required)"
    except:
        return "ERROR"
