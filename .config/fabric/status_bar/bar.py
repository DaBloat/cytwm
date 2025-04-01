from fabric.widgets.wayland import WaylandWindow as Window
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from status_bar.components.workspace import WorkSpace
from status_bar.components.profile import Profile, ProfileWidgets
from status_bar.components.settings import Settings, SettingsWidgets
from status_bar.components.misc import Separator


class StatusBar(Window):
    def __init__(self):
        super().__init__(
            monitor = 0,
            
            name = 'status-bar',
            layer = "bottom",
            exclusivity= "auto",
            anchor = "left top right",
            margin = '10px -5px 0px 12px',
            visible = False
        )
        
        self.profile_widget = ProfileWidgets(parent=self)
        self.profile_button = Profile(widget=self.profile_widget)
        self.profile_widget.set_pointing_to(self.profile_widget)
        
        self.setting_widget = SettingsWidgets(parent=self)
        self.setting_button = Settings(widget=self.setting_widget)
        self.setting_widget.set_pointing_to(self.setting_button)
        
        self.start = Box(
            name='start-box',
            children=[
                self.profile_button,
                Separator()
            ]
        )
        
        self.center = Box(
            children=[
                WorkSpace()
            ]
        )
        
        self.end = Box(
            name = 'end-box',
            children = [
                Separator(),
                self.setting_button
            ]
        )

        
        self.children = CenterBox(
            name='bar',
            start_children=self.start,
            center_children=self.center,
            end_children=self.end,
        )
        

        
        self.show_all()