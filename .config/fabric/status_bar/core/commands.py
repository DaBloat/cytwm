from getpass import getuser
from socket import gethostname
from psutil import boot_time
from time import time, sleep
from os import system


def get_user(self):
    return str(getuser()).capitalize()
    
def get_hostname(self):
    return str(gethostname())
    
def get_uptime(self):
    return self.update_uptime()
    
def update_uptime():
    time_decimal = str((time() - boot_time()) / 3600).split('.')
    split_time = str(float('.' + time_decimal[1]) * 60).split('.')
    time_decimal[1] = split_time[0]
    time_decimal.append(str(float('.' + split_time[1]) * 60).split('.')[0])
    return time_decimal
    
def power_off():
    return lambda x: system('systemctl poweroff')
    
def reboot():
    return lambda x: system('systemctl reboot')
    
def lock_system():
    return lambda x: system('echo Not Yet Finished')
