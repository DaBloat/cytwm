from fabric import Application
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.widgets.label import Label
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.box import Box
from fabric.widgets.datetime import DateTime
from fabric.system_tray.widgets import SystemTray
from fabric.widgets.button import Button
from fabric.hyprland.widgets import WorkspaceButton, Workspaces
from fabric.widgets.image import Image
from fabric.utils import get_relative_path
from components.buttons import *
from components.clock import *
from components.misc import *
from icons.directory import Icons

icon = Icons()

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

        self.active_clients = Button(
            name = 'active-clients-button',
            image = icon.menu
        )
        
        self.workspace = Workspaces(
            name = 'workspaces',
            spacing= 4,
            buttons = [WorkspaceButton(id=wd+1, label=None) for wd in range(5)],
            buttons_factory= lambda wd: WorkspaceButton(id=wd, label=None)
        )
        print(self.workspace._active_workspace)

        self.notifications = Button(
            name = 'notification-button',
            image = Image(
                    'icons/directory/notification.svg',
                    )
        )
        
        self.clock_info = ClockWidget(parent=self)
        self.clock = ClockButton(widget=self.clock_info)
        self.clock_info.set_pointing_to(self.clock)

        self.system_tray = SystemTray(
            name = 'sys-tray',
            spacing = 4,
            icon_size = 20
        )

        self.start = Button(
            name = 'start-button',
            image = Image(
                    'icons/directory/account.svg',
                    )
        )

        self.bluetooth = Button(
            name = 'bluetooth-button',
            image = Image(
                    'icons/directory/bluetooth.svg',
                    )
        )

        self.battery = BatteryButton()

        self.wifi = Button(
            name = 'wifi-button',
            image = Image(
                    'icons/directory/wifi.svg',
                    )
        )

        self.settings = Button(
            name = 'settings-button',
            image = Image(
                    'icons/directory/settings.svg',
                    )
        )
        
        self.applications = Button(
            name = 'applications-button',
            image = Image(
                    'icons/directory/app.svg',
                    )
        )


        self.children = CenterBox(
            name = 'bar',
            size = [60, 60],
            start_children = Box(
                name = 'left-container',
                children = [self.start,
                            Separator(),
                            self.applications,
                            Separator(),
                            Label('Spotify'),]
                    ),

            center_children = Box(
                name = 'middle-container',
                children = [self.active_clients,
                            Separator(),
                            self.workspace, 
                            Separator(),
                            self.notifications]),

            end_children = Box(
                name='right-container',
                children = [
                    self.system_tray,
                    Separator(),
                    self.bluetooth,
                    Separator(),
                    self.wifi,
                    Separator(),
                    self.battery,
                    Separator(),
                    self.clock,
                    Separator(),             
                    self.settings]
            )
        ) 

        self.show_all()

if __name__ == '__main__':
    bar = StatusBar()
    app = Application('status-bar', bar)
    app.set_stylesheet_from_file(get_relative_path("./style.css"))
    app.run()