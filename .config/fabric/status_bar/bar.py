from fabric.widgets.wayland import WaylandWindow as Window
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from status_bar.components.workspace import WorkSpace


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
        
        self.center = Box(
            children=[
                WorkSpace()
            ]
        )
        
        self.children = CenterBox(
            name='bar',
            start_children=Label('start'),
            center_children=self.center,
            end_children=Label('end'),
        )
        
        self.show_all()