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
        
        
class SettingsWidgets(PopupWindow):
    def __init__(self, parent):
        super().__init__(
            parent=parent,
            margin = '10px 10px',
            visible = False,
            all_visible = False)
        self.children = [TopBox()]
        
        
        
class TopBox(Box):
    def __init__(self):
        super().__init__(
            name='top-box',
            spacing = 5
        )
        
        self.change_theme = Button(
            name = 'change-theme-button',
            child = Label('󰄛')
        )
        
        self.screen_record = Button(
            name = 'screen-record-button',
            child = Label(''),
        )
        
        self.screen_shot = Button(
            name = 'screen-shot-button',
            child = Label('')
        )
        
        self.game_mode = Button(
            name = 'game-mode-button',
            child = Label('󰊗')
        )
        
        self.set_button = Button(
            name = 'set-button',
            child = Label('')
        )
              
        
        self.children = [self.change_theme,
                         self.screen_record,
                         self.screen_shot,
                         self.game_mode,
                         self.set_button]
        


