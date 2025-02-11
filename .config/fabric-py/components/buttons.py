from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from datetime import datetime
from fabric.widgets.image import Image
from fabric.utils import invoke_repeater


class ClockButton(Button):
    def __init__(self):
        super().__init__(
            name='clock-button',
        )
        self.time = Label()
        self.children = self.time
        
        invoke_repeater(1000, self.update_time)
        
        
    def update_time(self):
        self.time.set_label(f'{datetime.now().strftime('%I:%M %p')}')
        return True
        
        
        