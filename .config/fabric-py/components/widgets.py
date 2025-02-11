from components.popups import PopupWindow
from fabric.widgets.label import Label
from fabric.widgets.box import Box

class TimeAndDate(PopupWindow):
    def __init__(self, parent):
        super().__init__(parent,
                         visible = False,
                         all_visible = False
                         )
        
        self.box = Box(name='try', children=[Label('Trial'), Label("Trial")])
        self.children = self.box