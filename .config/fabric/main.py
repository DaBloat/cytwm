from status_bar.bar import StatusBar
from fabric import Application
from fabric.utils import monitor_file, invoke_repeater, get_relative_path

def set_css(*_):
        return app.set_stylesheet_from_file(
            get_relative_path("main.css")
    )

if __name__ == '__main__':
    bar = StatusBar()
    app = Application('status-bar', bar)
    
    monitor = monitor_file(get_relative_path('style/cyna-colors.css'))
    monitor.connect('changed', set_css)
    set_css()
    app.run()