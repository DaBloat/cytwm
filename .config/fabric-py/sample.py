import fabric
from fabric import Application, Fabricator
from fabric.widgets.datetime import DateTime
from fabric.widgets.label import Label
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.widgets.centerbox import CenterBox
from datetime import datetime

class UpdateClock(Fabricator):
    def __init__(self):
        super().__init__(
            interval = 1000,
            poll_from = 'date',
            on_changed = lambda f, v: print(f"Current Date: {v.strip()}")
        )
       
class Clock(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer='background',
            anchor='top',
            **kwargs
        )


        self.children = CenterBox(DateTime())

if __name__ == '__main__':
    p = UpdateClock()
    clock = Clock()
    app = Application('clock', clock)
    app.run()

