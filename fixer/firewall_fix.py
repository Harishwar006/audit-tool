import subprocess

def fix_firewall():
    subprocess.call("ufw --force enable", shell=True)
