import flet as ft


class PathVisualisation(ft.Column):
    def __init__(self):
        super().__init__()

        self.text_size = 20
        self.alignment = ft.MainAxisAlignment.CENTER

        self.text=ft.Text("Path", size=self.text_size)


        self.controls = [
            self.text,
            self.text,
            self.text
        ]

    def set_path(self, path):
        pass # я задовбався писати цей код, але ви зрозуміли ідею