import flet as ft


class DialogWindow(ft.Container):
    def __init__(self):
        self.message = ft.Text("Dialog window", size=20, color=ft.colors.BLACK)
        self.ok_button = ft.ElevatedButton("OK", width=80, height=30, on_click=lambda _: self.hide())
        self.window = ft.Container(
            ft.Row(
                [self.message,
                 self.ok_button, ],
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True,
            ),
            padding=10,
            border_radius=ft.border_radius.all(10),
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(2, "RED"),
        )

        super().__init__(self.window)
        self.alignment = ft.alignment.center
        self.expand = True
        self.visible = False
        self.height = 500 # єбать я костиль вєбав

    def set_message(self, message):
        print(message)
        self.message.value = message

    def show(self):
        print("Showing dialog")
        self.visible = True
        self.update()

    def hide(self):
        print("Hiding dialog")
        self.visible = False
        self.update()
