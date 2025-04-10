from status_bar.components.misc import PopupWindow
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.circularprogressbar import CircularProgressBar
from fabric.widgets.overlay import Overlay
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
        elif int(minute) == 0:
            self.top.set_label(hour + s_strs(int(hour), "hour"))
            self.bot.set_label(seconds + s_strs(int(seconds), "second"))
        else:
            self.top.set_label(hour + s_strs(int(hour), "hour"))
            self.bot.set_label(minute + s_strs(int(minute), "minute"))
        self.top.set_style('font-size: 16px; color: var(--foreground);')
        self.bot.set_style('font-size: 16px; color: var(--foreground);')
        return True
    
    
class HardwareInfo(Box):
    def __init__(self):
        super().__init__(
            name = 'hardware-info',
            h_align = 'center',
            h_expand = True
        )
        
        self.children = Box(spacing = 10, 
                            style='margin: 5px 10px;',
                            children=[CPUBar(), MemoryBar(), DiskBar(), GPUBar()])
        
class CPUBar(Box):
    def __init__(self):
        super().__init__(
            orientation='v'
        )
        self.cpu = CircularProgressBar(
            name = 'cpu-progress-bar',
            pie = False,
            size = 42
        )
        self.cpu_progress = Overlay(
            child = self.cpu,
            overlays = [Label("", name = 'cpu-logo')]
        )
        self.label = Label('CPU', name = 'cpu-label')
        self.children = [self.cpu_progress, self.label]
        invoke_repeater(1000, self.update_percent)
        
        
    def update_percent(self):
        self.cpu.value = commands.get_cpu_usage()
        return True
    

class MemoryBar(Box):
    def __init__(self):
        super().__init__(
            orientation='v'
        )
        self.mem = CircularProgressBar(
            name = 'mem-progress-bar',
            pie = False,
            size = 42
        )
        self.mem_progress = Overlay(
            child = self.mem,
            overlays = [Label("", name = 'mem-logo')]
        )
        self.label = Label('MEMORY', name = 'mem-label')
        self.children = [self.mem_progress, self.label]
        invoke_repeater(1000, self.update_percent)
        
        
    def update_percent(self):
        self.mem.value = commands.get_mem_usage()
        return True
    
    
class DiskBar(Box):
    def __init__(self):
        super().__init__(
            orientation='v'
        )
        self.disk = CircularProgressBar(
            name = 'disk-progress-bar',
            pie = False,
            size = 42
        )
        self.disk_progress = Overlay(
            child = self.disk,
            overlays = [Label("󰋊", name = 'disk-logo')]
        )
        self.label = Label('DISK', name = 'disk-label')
        self.children = [self.disk_progress, self.label]
        invoke_repeater(1000, self.update_percent)
        
        
    def update_percent(self):
        self.disk.value = commands.get_disk_usage()
        return True
    

class GPUBar(Box):
    def __init__(self):
        super().__init__(
            orientation='v'
        )
        self.gpu = CircularProgressBar(
            name = 'gpu-progress-bar',
            pie = False,
            size = 42
        )
        self.gpu_progress = Overlay(
            child = self.gpu,
            overlays = [Label("󰆨", name = 'gpu-logo')]
        )
        self.label = Label('GPU', name = 'gpu-label')
        self.children = [self.gpu_progress, self.label]
        invoke_repeater(1000, self.update_percent)
        
        
    def update_percent(self):
        self.gpu.value = commands.get_gpu_utilization()
        return True


class LinuxDistro(Box):
    def __init__(self):
        super().__init__(
            name = 'linux-distro',
        )   
        self.children = [Label('󰣇', name='linux-distro-logo')]
    
    
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
        
        self.bot_right_box = Box(
            children = [HardwareInfo()]
        )
        
        self.bot_left_box = Box(
            children = [LinuxDistro()]
        )
        
        self.bot_box = Box(
            spacing = 10,
            children = [self.bot_right_box, self.bot_left_box]
        )
        

        self.children = Box(
            orientation= 'v',
            spacing = 10,
            children=[self.top_box, self.bot_box]
        )