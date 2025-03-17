from fabric.widgets.button import Button
from fabric.widgets.label import Label
from fabric.widgets.box import Box
from status_bar.components.misc import PopupWindow


class Setting(Button):
    def __init__(self):
        super().__init__(
            name = 'setting',
            on_clicked = lambda *_ : 0
        )
        

