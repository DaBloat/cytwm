import fabric
from fabric import Application
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.widgets.label import Label
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.box import Box
from fabric.widgets.datetime import DateTime
from fabric.system_tray.widgets import SystemTray
from fabric.utils import get_relative_path


class StatusBar(Window):
    def __init__(self):
        super().__init__(
            monitor = 0,
            name = 'status-bar',
            layer = "top",
            exclusivity= "auto",
            anchor = "left top right",
            margin = '10px -5px 0px 12px',
            visible = False
        )

        self.seperators = Label(
            '|',
            name = 'seperators'
        )

        self.clock = DateTime(
            name = 'clock'
        )

        self.system_tray = SystemTray(
            name = 'sys-tray',
            spacing = 4,
            icon_size = 20
        )

        self.children = CenterBox(
            name = 'bar',
            size = [55, 55],
            start_children = Box(
                name = 'left-container',
                children = [Label("1"), Label('2')]),

            center_children = Box(
                name = 'middle-container',
                children = [Label('|', name='seperators'), self.system_tray, Label('|', name='seperators')]),

            end_children = Box(
                name='right-container',
                children = [self.clock]
            )
        ) 

        self.show_all()

if __name__ == '__main__':
    bar = StatusBar()
    app = Application('status-bar', bar)
    app.set_stylesheet_from_file(get_relative_path("./style.css"))
    app.run()