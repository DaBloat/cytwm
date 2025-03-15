from status_bar.components.misc import PopupWindow
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from status_bar.components.misc import RoundedImage
from fabric.utils import get_relative_path, invoke_repeater
import getpass, socket, os, psutil, time, subprocess

class Profile(Button):
    def __init__(self, widget=None):
        super().__init__(
            name='profile',
            on_clicked = lambda *_ : widget.show() if not widget.is_visible() else widget.hide() 
        )
        self.children = Label('')
        
class ProfileWidgets(PopupWindow):
    def __init__(self, parent):
        super().__init__(
            parent=parent,
            margin='10px 0px',
            visible = False,
            all_visible = False)
    
        self.pfp = Box(
            name = 'pfp',
            children = RoundedImage(
                        get_relative_path('profile.png'),
                        size = [60, 60],
                    )
                )
        
        self.power_button = Button(
            name='power-button',
            child = Label(''),
            size = [50, 50],
            on_clicked = lambda x : os.system('sudo systemctl poweroff')
            )
        
        self.reboot_button = Button(
            name='reboot-button',
            child = Label('󰜉'),
            size = [50, 50],
            on_clicked = lambda x : os.system('sudo systemctl reboot')
        )
        
        self.lock_button = Button(
            name='lock-button',
            child = Label(''),
            size = [50, 50],
            on_clicked = lambda x : print('still in progress!')
        )

        self.uptime = Label()
        self.children = Box(
                children=[self.left_wing(), self.middle_wing(), self.right_wing()]
        )
        
        invoke_repeater(1000, self.uptime_update)
        
    def uptime_update(self):
        uptime = str((time.time() - psutil.boot_time()) / 3600).split('.')
        hour = int(uptime[0])
        minute = int(float('.'+uptime[1]) * 60)
        if hour == 0 and minute == 0:
            self.uptime.set_label("< 1 min")
            self.uptime.set_style('color: var(--foreground); margin: 0px 40px;')
        elif hour == 0 and minute > 0:
            self.uptime.set_label(f"{self.mins_(minute)}")
            self.uptime.set_style('color: var(--foreground); margin: 0px 40px;')
        elif hour > 0 and minute == 0:
            self.uptime.set_label(f"{self.hour_(hour)}")
            self.uptime.set_style('color: var(--foreground); margin: 0px 40px;')
        elif (hour // 10) <= 0:
            self.uptime.set_label(f"{self.hour_(hour)}, {self.mins_(minute)}")
            self.uptime.set_style('color: var(--foreground); margin: 0px 10px;')
        else:
            self.uptime.set_label(f"{self.hour_(hour)}, {self.mins_(minute)}")
            self.uptime.set_style('color: var(--foreground);')
        return True
    
    def hour_(self, hr):
        if hr > 1:
            return f'{hr} hours'
        elif hr == 1:
            return f'{hr} hour'
        else:
            return ''
        
    def mins_(self, min):
        if min > 1:
            return f'{min} mins'
        elif min == 1:
            return f'{min} min'
        else:
            return ''           
        
    def left_wing(self):
        self.whoami = Box(
            orientation='v',
            name='whoami',
            children=[self.pfp, 
                      Label(f'{str(getpass.getuser()).capitalize()}', name='user'),
                      Label(f'{socket.gethostname()}', name='hostname')]    
        )       
        
        return Box(
            orientation='v',
            children=[self.whoami]
        )
    
    def middle_wing(self):
        self.uptime_box = Box(
            name='uptime-box',

            children=[ Label('Up: ', name='uptime-label'), self.uptime]
        )
        
        self.button_box = Box(
            name =  'button-box',
            children=[self.lock_button, self.reboot_button, self.power_button]
        )
    
        
        self.pacman_packages = Box(
            name='pacman-packages',
            children= [
                Label('󰣇'),
                Label(f"{subprocess.check_output('sudo pacman -Q | wc -l', shell=True)}".split("'")[1].strip('\\n'))
            ]
        )
        
        self.pacman_updates = Box(
            name = 'pacman-updates',
            children = [
                Label('󱧘'),
                Label(f"{subprocess.check_output('checkupdates | wc -l', shell=True)}".split("'")[1].strip('\\n'))
            ]
        )
        
        self.aur_updates = Box(
            name = 'aur-updates',
            children = [
                Label('󰏖'),
                Label(f"{subprocess.check_output('yay -Qum | wc -l', shell=True)}".split("'")[1].strip('\\n'))
            ]
        )
        
        self.pacman_box = Box(
            name = 'pacman-box',
            size = [100, 15],
            children = [self.pacman_packages, self.pacman_updates, self.aur_updates]
        )
        
        return Box(
            orientation='v',
            v_align='start',
            children=[self.uptime_box, self.button_box, self.pacman_box]
        )
    
    def right_wing(self):
        return Box(
            children=Label('right'),
        )        
        
    
