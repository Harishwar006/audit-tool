import subprocess

def fix_ssh():
    subprocess.call("sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config", shell=True)
    subprocess.call("sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config", shell=True)
    subprocess.call("systemctl restart ssh", shell=True)
