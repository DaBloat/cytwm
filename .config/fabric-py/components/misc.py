from fabric.widgets.label import Label


class Separator(Label):
    def __init__(self):
        super().__init__(
            '|',
            name = 'separators',
        )