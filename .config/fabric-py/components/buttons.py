import subprocess
from datetime import datetime
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.image import Image
from fabric.widgets.circularprogressbar import CircularProgressBar
from fabric.utils import invoke_repeater

class ClockButton(Button):
    def __init__(self, widget=None):
        super().__init__(
            name='clock-button',
            on_clicked = lambda *_ : widget.show() if not widget.is_visible() else widget.hide() 
        )
        self.time = Label()
        self.children = self.time
        
        invoke_repeater(1000, self.update_time)
        
        
    def update_time(self):
        self.time.set_label(f'{datetime.now().strftime('%I:%M %p')}')
        return True
    
class BatteryButton(Button):
    def __init__(self, widget=None):
        super().__init__(
            name='battery-button',
            on_clicked = lambda *_ : widget.show() if not widget.is_visible() else widget.hide() 
        )
        
        self.percent = Label()
        self.icon = {'Discharging':Image('icons/directory/battery.svg'), 
                     'Charging':Image('icons/directory/battery_charging.svg'), 
                     'Full':Image('icons/directory/battery_charging.svg'),
                     'Not charging':Image('icons/directory/battery.svg')}
        
        self.battery_icon = Box()
        self.battery_percent = Box(children=self.percent)
        
        self.children = Box(v_expand=True, v_align='center', children=[self.battery_icon, self.battery_percent])
        
        invoke_repeater(1000, self.display_battery)
        
    def fetch_status(self):
        status = subprocess.run("cat /sys/class/power_supply/BAT1/status",
                                 capture_output=True,
                                 text=True, 
                                 shell=True).stdout.strip()
        return status
    
    def fetch_percentage(self):
        percent = subprocess.run("cat /sys/class/power_supply/BAT1/capacity",
                                 capture_output=True,
                                 text=True, 
                                 shell=True).stdout.strip()
        return percent
        
    def display_battery(self):
        self.percent.set_label(f'{self.fetch_percentage()}%')
        self.battery_icon.children = self.icon[self.fetch_status()]
        return True

        
        
        