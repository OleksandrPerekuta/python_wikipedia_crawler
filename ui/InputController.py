import flet as ft

from ui.DialogWindow import DialogWindow
from ui.PathVisualisation import PathVisualisation


class InputController(ft.Column):
    def __init__(self, page: ft.Page, visualisation_column: PathVisualisation, dialog: DialogWindow):
        super().__init__()
        self.page = page
        self.visualisationColumn = visualisation_column
        self.dialog = dialog

        self.alignment = ft.MainAxisAlignment.CENTER
        self.text_size = 20
        self.expand = True
        self.height_factor = 0.9
        self.width_factor = 0.25

        self.targetText = ft.Text("Target page:", size=self.text_size, width=120)
        self.targetInput = ft.TextField(hint_text="Enter URL")
        self.targetRow = ft.Row(
            [
                self.targetText,
                self.targetInput,
            ],
        )

        self.sourceText = ft.Text("Source page:", size=self.text_size, width=120)
        self.sourceInput = ft.TextField(hint_text="Enter URL")
        self.sourceRow = ft.Row(
            [
                self.sourceText,
                self.sourceInput,
            ],
        )

        self.searchButton = ft.ElevatedButton("Search", width=120, height=40, on_click=lambda _: self.search())

        self.border_radius = ft.border_radius.all(10)
        self.controls = [
            self.targetRow,
            self.sourceRow,
            self.searchButton,
        ]

    def search(self):
        valid = self.validate_links(self.targetInput.value, self.sourceInput.value)

        if not valid:
            self.dialog.set_message("Invalid links")
            self.dialog.show()
            return

        try:
            pass # тут будемо викликати функцію пошуку шляху

        except Exception as e:
            self.dialog.set_message(e.__str__())
            self.dialog.show()


    def validate_links(self, target, source):
        if not target or not source:
            return False

        if not target.startswith("https://en.wikipedia.org/wiki/") or not source.startswith("https://en.wikipedia.org/wiki/"):
            return False

        return True