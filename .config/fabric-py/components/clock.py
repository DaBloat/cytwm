from fabric import Application
from fabric.widgets.button import Button
from fabric.widgets.label import Label
from fabric.widgets.box import Box
from fabric.widgets.centerbox import CenterBox
from datetime import datetime
from components.popups import PopupWindow
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
    
class ClockWidget(PopupWindow):
    def __init__(self, parent, pointing_to = None):
        super().__init__(parent,
                         pointing_to,
                         margin = '10px',
                         name='clock-widget',
                         visible = False,
                         all_visible = False)
        self.calendar = Calendar()
        self.activities = Activities()
        self.uptime = Uptime()
        self.left = Box(orientation='v', children=[self.calendar])
        self.right = Box(orientation='v', children=[self.activities, self.uptime])
        self.children = CenterBox(size=[350, 130], h_expand=True, v_expand=True, start_children=[self.left, self.right])
        
class Calendar(Box):
    def __init__(self):
        super().__init__(
            name='calendar-box',
            size=[130,130]
        )
        self.children = [Label('Calendar')]
        
class Activities(Box):
    def __init__(self):
        super().__init__(
            name='activities-box',
            size=[220,100]
        )
        self.children = [Label('Activities')]

class Uptime(Box):
    def __init__(self):
        super().__init__(
            name='uptime-box',
            size=[220,20]
        )
        self.children = [Label('uptime')]
        