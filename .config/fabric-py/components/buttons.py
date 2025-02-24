import subprocess
from datetime import datetime
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.image import Image
from fabric.widgets.circularprogressbar import CircularProgressBar
from fabric.utils import invoke_repeater
    
class BatteryButton(Button):
    def __init__(self, widget=None):
        super().__init__(
            name='battery-button',
            on_clicked = lambda *_ : widget.show() if not widget.is_visible() else widget.hide() 
        )
        
        self.percent = Label()
        self.icons = {'05 - c':Image('icons/battery/battery-charging-5.svg'), 
                      '05 - nc':Image('icons/battery/battery-5.svg'),
                      '2 - c':Image('icons/battery/battery-charging-20.svg'), 
                      '2 - nc':Image('icons/battery/battery-20.svg'), 
                      '3 - c':Image('icons/battery/battery-charging-30.svg'), 
                      '3 - nc':Image('icons/battery/battery-30.svg'), 
                      '5 - c':Image('icons/battery/battery-charging-50.svg'), 
                      '5 - nc':Image('icons/battery/battery-50.svg'),
                      '6 - c':Image('icons/battery/battery-charging-60.svg'), 
                      '6 - nc':Image('icons/battery/battery-60.svg'),
                      '8 - c':Image('icons/battery/battery-charging-80.svg'), 
                      '8 - nc':Image('icons/battery/battery-80.svg'),
                      '9 - c':Image('icons/battery/battery-charging-90.svg'), 
                      '9 - nc':Image('icons/battery/battery-90.svg'),
                      'full - c':Image('icons/battery/battery-charging-full.svg'), 
                      'full - nc':Image('icons/battery/battery-full.svg'),}
        
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
        return int(percent)
    
    def fetch_boundary(self, val:int):
        indiv = [2, 5, 8, 9]
        if val <= 1:
            return '05'
        elif val <= 4 and val not in indiv:
            return '3'
        elif val <= 7 and val not in indiv:
            return '6'
        elif val == 10:
            return 'full'
        else:
            return f'{val}'
    
    def fetch_state(self):
        non_charging_state = ('Discharging', 'Not charging')
        charging_state = ('Full', 'Charging')
        if self.fetch_status() in non_charging_state:
            return f'{self.fetch_boundary(int(self.fetch_percentage() / 10))} - nc'
        
        elif self.fetch_status() in charging_state:
            return f'{self.fetch_boundary(int(self.fetch_percentage() / 10))} - c'


    def display_battery(self):
        self.percent.set_label(f'{self.fetch_percentage()}%')
        # print(self.fetch_boundary(self.fetch_state()))
        self.battery_icon.children = self.icons[self.fetch_state()]
        return True

        
        
        