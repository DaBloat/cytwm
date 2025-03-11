from status_bar.components.misc import PopupWindow
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label

class Profile(Button):
    def __init__(self, widget=None):
        super().__init__(
            name='profile',
            on_clicked = lambda *_ : widget.show() if not widget.is_visible() else widget.hide() 
        )
        self.children = Label('')
        
class ProfileWidgets(PopupWindow):
    def __init__(self, parent):
        super().__init__(
            parent=parent,
            visible = False,
            all_visible = False)
        
        self.children = Box(
                children=[self.left_wing(), self.middle_wing(), self.right_wing()]
        )
        
    def left_wing(self):
        return Box(
            children=Label('left')
        )
    
    def middle_wing(self):
        return Box(
            children=Label('middle')
        )
    
    def right_wing(self):
        return Box(
            children=Label('right')
        )        
        
    
