from fabric.widgets.button import Button
from fabric.widgets.label import Label
from fabric.widgets.box import Box
from status_bar.components.misc import PopupWindow


class Settings(Button):
    def __init__(self, widget=None):
        super().__init__(
            name = 'settings',
            on_clicked = lambda *_ : widget.show() if not widget.is_visible() else widget.hide()
        )
        self.children = Label('')
        

class WifiSettings(Button):
    def __init__(self):
        super().__init__(
            name = 'wifi-button'
        )
        self.children = Label('󰤨')
        
class BluetoothSettings(Button):
    def __init__(self):
        super().__init__(
            name = 'bluetooth-button'
        )
        self.children = Label('󰂯')
        
class ThemeSettings(Button):
    def __init__(self):
        super().__init__(
            name = 'theme-button'
        )
        self.children = Label('󰄛')
            
class ButtonBox(Box):
    def __init__(self):
        super().__init__(
            name = 'button-box'
        )
        self.children = [WifiSettings(), BluetoothSettings(), ThemeSettings()]
    
        
class SettingsWidgets(PopupWindow):
    def __init__(self, parent):
        super().__init__(
            parent=parent,
            margin = '10px 10px',
            visible = False,
            all_visible = False)
        self.children = [ButtonBox()]
