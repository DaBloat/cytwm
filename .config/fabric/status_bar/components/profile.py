from status_bar.components.misc import PopupWindow
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from status_bar.components.misc import RoundedImage
from fabric.utils import get_relative_path, invoke_repeater
import getpass, socket, os, psutil, time

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
            margin='10px',
            visible = False,
            all_visible = False)
        
        self.pfp = Box(
            name = 'pfp',
            children = RoundedImage(
                        get_relative_path('profile.png'),
                        size = [60, 60],
                    )
                )
        
        
        self.children = Box(
                children=[self.left_wing(), self.middle_wing(), self.right_wing()]
        )
        
        invoke_repeater(1000, self.uptime_update)
        
        
    def uptime_update(self):
        uptime = str((time.time() - psutil.boot_time()) / 3600).split('.')
        hour = int(uptime[0])
        minute = int(float('.'+uptime[1]) * 60)
        if hour > 0 and minute == 0:
            self.uptime.set_label(f"{self.hour_(hour)}")
        else:
            self.uptime.set_label(f"{self.hour_(hour)}{self.mins_(minute)}")
        return True
    
    def hour_(self, hr):
        if hr > 1:
            return f'{hr} hours '
        elif hr == 1:
            return f'{hr} hour '
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
        self.uptime = Label(name='uptime')
        self.uptime_box = Box(
            orientation='v',
            name='uptime-box',
            children=[self.uptime, Label('Uptime', name='uptime-label')]
        )
        
        return Box(
            v_align='start',
            children=[self.uptime_box]
        )
    
    def right_wing(self):
        return Box(
            children=Label('right')
        )        
        
    
