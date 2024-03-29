import os

print("\t\t    +------------------+")
print("\t\t    |   SwitchX v1.0   |")
print("\t\t    +------------------+")
print("\t\t    (c) Aodrulez\n")
print("( Adds support for XBOX360 controllers to Nintendo Switch )\n")
if not os.geteuid() == 0:
	raise PermissionError(' [-] Script must be run as root/sudo!')
print("[+] Installing required packages/libraries & setting up everything!\n\n")
os.system("apt-get -o Acquire::ForceIPv4=true update")
os.system("apt-get -o Acquire::ForceIPv4=true install -y python3 python3-pip xboxdrv python3-dbus supervisor")
os.system("pip3 install hid aioconsole dbus-python")
os.system('echo "[program:switchX]" > /etc/supervisor/conf.d/switchX.conf')
os.system('echo "priority=10" >> /etc/supervisor/conf.d/switchX.conf')
os.system('echo "directory='+os.getcwd()+'" >> /etc/supervisor/conf.d/switchX.conf')
os.system('echo "command=python3 switchX.py" >> /etc/supervisor/conf.d/switchX.conf')
os.system('echo "user=root" >> /etc/supervisor/conf.d/switchX.conf')
os.system('echo "autostart=true" >> /etc/supervisor/conf.d/switchX.conf')
os.system('echo "autorestart=true" >> /etc/supervisor/conf.d/switchX.conf')
print("[+] Done.")
print("[+] Reboot now!")
