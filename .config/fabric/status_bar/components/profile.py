from status_bar.components.misc import PopupWindow
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from status_bar.components.misc import RoundedImage
from fabric.utils import get_relative_path, invoke_repeater
from status_bar.core import commands
import getpass, socket, os, psutil, time


class Profile(Button):
    def __init__(self, widget=None):
        super().__init__(
            name = 'profile',
            on_clicked = lambda *_ : widget.show() if not widget.is_visible() else widget.hide() 
        )
        self.children = Label('')
 
        
class UserInfo(Box):
    def __init__(self):
        super().__init__(
            orientation = 'v',
            name = 'whoami',
        )
        self.pfp = Box(
            name = 'pfp',
            children = RoundedImage(
                        get_relative_path('profile.png'),
                        size = [60, 60]))
        self.children = [self.pfp, 
                        Label(commands.get_user(), name='user'),
                        Label(commands.get_hostname(), name='hostname')]
        
class PowerButton(Button):
    def __init__(self):
        super().__init__(
            name = 'power-button',
            size = [50, 50],
            on_clicked = commands.power_off(),
            child = Label('')
        )


class RebootButton(Button):
    def __init__(self):
        super().__init__(
            name = 'reboot-button',
            size = [50, 50],
            on_clicked = commands.reboot(),
            child = Label('󰜉')
        )
        
        
class LockButton(Button):
    def __init__(self):
        super().__init__(
            name = 'lock-button',
            size = [50, 50],
            on_clicked = commands.lock_system(),
            child = Label('')
        )
        
        
class ButtonShelf(Box):
    def __init__(self):
        super().__init__(
            name = 'button-shelf',
            spacing = 10
        )
        self.children = [LockButton(), RebootButton(), PowerButton()]
        
        
class UptimeInfo(Box):
    def __init__(self):
        super().__init__(
            name='uptime-info',
        )
        self.logo = Label('', name = 'uptime-logo')
        self.top = Label()
        self.bot = Label()
        self.uptime = Box(
            orientation = 'v',
            h_align = 'center',
            v_align = 'center',
            children = [self.top, self.bot]
        )
        self.children = [self.logo, self.uptime]
        invoke_repeater(1000, self.update_labels)
        
    def update_labels(self):
        [hour, minute, seconds] = commands.update_uptime()
        s_strs = lambda val, tim: f" {tim}" if val <= 1 else f" {tim}s"
        if int(hour) == 0:
            self.top.set_label(minute + s_strs(int(minute), "minute"))
            self.bot.set_label(seconds + s_strs(int(seconds), "second"))
        else:
            self.top.set_label(hour + s_strs(int(hour), "hour"))
            self.bot.set_label(minute + s_strs(int(minute), "minute"))
        self.top.set_style('font-size: 16px; color: var(--foreground);')
        self.bot.set_style('font-size: 16px; color: var(--foreground);')
        return True

    
class ProfileWidgets(PopupWindow):
    def __init__(self, parent):
        super().__init__(
            parent=parent,
            margin='10px 0px',
            visible = False,
            all_visible = False)
        self.top_left_side = Box(
            orientation = 'v',
            children = [UserInfo()]
        )
        self.top_right_side = Box(
            orientation='v',
            align='start',
            spacing = 10,
            children=[ButtonShelf(), UptimeInfo()]
        )
        
        self.top_box = Box(
            spacing = 10,
            children = [self.top_left_side, self.top_right_side]
        )

        self.children = Box(
                children=[self.top_box]
        )