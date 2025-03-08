from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label

class Profile(Button):
    def __init__(self):
        super().__init__(
            name='profile'
        )
        self.children = Label('')
        
class ProfileWidgets:
    def __init__(self):
        pass
    
