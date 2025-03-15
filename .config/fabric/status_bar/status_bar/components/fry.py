import subprocess

print(f'{subprocess.check_output('sudo pacman -Q | wc -l', shell=True)}'.split("'")[1].strip('\\n'))