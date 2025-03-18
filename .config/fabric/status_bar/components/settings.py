from fabric.widgets.button import Button
from fabric.widgets.label import Label
from fabric.widgets.box import Box
from status_bar.components.misc import PopupWindow


class Settings(Button):
    def __init__(self, widget=None):
        super().__init__(
            name = 'settings',
            on_clicked = lambda *_ : widget.show() if not widget.is_visible else widget.hide()
        )
        self.children = Label('')
    
class SettingsWidgets(PopupWindow):
    def __init__(self, parent):
        super().__init__(parent=parent)
        
    
        

