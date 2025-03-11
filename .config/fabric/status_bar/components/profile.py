from status_bar.components.misc import PopupWindow
from fabric.widgets.button import Button
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from status_bar.components.misc import RoundedImage
from fabric.utils import get_relative_path
import cairo
import getpass

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
            margin='10px',
            visible = False,
            all_visible = False)
        
        self.pfp = Box(
            name = 'pfp',
            children = RoundedImage(
                        get_relative_path('profile.png'),
                        size = [60, 60],
                    )
                )
        
        
        self.children = Box(
                children=[self.left_wing(), self.middle_wing(), self.right_wing()]
        )
        
    def left_wing(self):
        self.whoami = Box(
            orientation='v',
            name='whoami',
            children=[self.pfp, 
                      Label(f'{str(getpass.getuser()).capitalize()}', name='user'),
                      Label('DaBloat', style='font-size: 12px; ', name='alias')]    
        )
        return Box(
            children=[self.whoami]
        )
    
    def middle_wing(self):
        return Box(
            children=Label('middle')
        )
    
    def right_wing(self):
        return Box(
            children=Label('right')
        )        
        
    
