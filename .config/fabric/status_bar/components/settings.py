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
        self.children = [Label('')]
        
        
class SettingLabelBox(Box):
    def __init__(self):
        super().__init__(
            name = 'setting-label-box',
            size = [100, 20],
            h_align = 'center'
        )
        self.children = Label('Settings', name = 'setting-label')
        

class WifiSettings(Button):
    def __init__(self):
        super().__init__(
            name = 'wifi-button',
            size = [125, 100],
            v_align = 'center'
        )
        self.icon = Label('󰤨')
        self.icon.set_style("font-size: 40px; font-family: 'NotoSansM Nerd Font Propo'; margin: 0 5px;")
        self.wifi = Label('Wifi')
        # VILLAMOR_PRINT
        # VILLAMOR_5G
        # T.I.P.ian Student
        # T.I.P.ian Employee
        self.wifi.set_style('font-size: 12px;')
        self.state = Label('On')
        self.state.set_style('font-size: 10px;')
        self.children = Box(
            orientation= 'v',
            children=[self.icon, self.wifi, self.state]
            )
        
             

        
class BluetoothSettings(Button):
    def __init__(self):
        super().__init__(
            name = 'bluetooth-button'
        )
        self.children = Label('󰂯')
        
class AudioSettings(Button):
    def __init__(self):
        super().__init__(
            name = 'audio-button'
        )
        self.children = Label('')

            
class ButtonBox(Box):
    def __init__(self):
        super().__init__(
            name = 'button-box',
            orientation = 'v'
        )
        self.children = [WifiSettings()]
        
class PlaceHolderBox(Box):
    def __init__(self):
        super().__init__(
            name = 'test',
            size = [207, 170]
        )
        
        
class SettingsWidgets(PopupWindow):
    def __init__(self, parent):
        super().__init__(
            parent=parent,
            margin = '10px 10px',
            visible = False,
            all_visible = False)
        
        self.top_box = Box(
            name = 'top-box',
            children = [SettingLabelBox()]
        )
        
        self.bot_box = Box(
            name = 'bot-box',
            children = [ButtonBox()]
        )
        
        self.children = Box(
            orientation='v',
            children=[self.top_box, 
                      self.bot_box])
