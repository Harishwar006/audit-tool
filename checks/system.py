def audit_system():
    try:
        with open("/proc/sys/kernel/randomize_va_space") as f:
            return "PASS" if f.read().strip() == "2" else "FAIL (Manual Fix)"
    except:
        return "ERROR"
