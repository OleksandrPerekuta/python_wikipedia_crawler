import flet as ft

from ui.DialogWindow import DialogWindow
from ui.InputController import InputController
from ui.PathVisualisation import PathVisualisation


def main(page: ft.Page):
    page.title = "Wikipedia crawler"

    dialog = DialogWindow()
    visualisation_column = PathVisualisation()
    input_controller = InputController(page, visualisation_column, dialog)

    row = ft.Row(
        [
            ft.Container(
                input_controller,
                padding=10,
                margin=5,
                border_radius=ft.border_radius.all(10),
                border=ft.border.all(2),
                height=page.height - 50,
            ),
            ft.Container(
                visualisation_column,
                padding=10,
                margin=5,
                height=page.height - 50,
                alignment=ft.alignment.center,
                expand=True,
                border_radius=ft.border_radius.all(10),
                border=ft.border.all(2),

            ),
        ],
    )
    row.visible = True

    stack = ft.Stack(
        [
            row,
            dialog,
        ],
        alignment=ft.alignment.center,
        fit=ft.StackFit.PASS_THROUGH,
    )

    page.add(
        stack
    )



if __name__ == "__main__":
    ft.app(main)

