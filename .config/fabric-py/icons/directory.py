from fabric.widgets.image import Image
from fabric.utils import get_relative_path

class Icons:
    def __init__(self):
        self.menu = Image(get_relative_path('directory/menu.svg'))