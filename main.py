import flet as ft

from ui.DialogWindow import DialogWindow
from ui.InputController import InputController
from ui.PathVisualisation import PathVisualisation


def main(page: ft.Page):
    """
   Initialize the Flet app with a UI for a Wikipedia crawler. This function sets up the user interface
   components and interactions on the provided Flet page.

   Args:
   page (ft.Page): The main page of the Flet application where UI components are added.

   This function creates and configures the following UI components:
   - DialogWindow: A modal dialog window for displaying error messages.
   - PathVisualisation: A component for visualizing the path of Wikipedia pages crawled.
   - InputController: A controller to handle user inputs and control other UI components.
   """
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

