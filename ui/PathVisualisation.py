import time
import webbrowser

import flet as ft


class PathVisualisation(ft.Column):
    def __init__(self):
        super().__init__()

        self.text_size = 20
        self.alignment = ft.MainAxisAlignment.CENTER
        self.spacing = 0
        self.width = 200
        self.scroll = ft.ScrollMode.ALWAYS

    def add_node(self, node: tuple[str, str], to_paint: bool = True):
        if to_paint:
            line = ft.Container(
                width=2,
                height=60,
                margin=ft.margin.only(left=50, top=0, bottom=0),
                bgcolor=ft.colors.WHITE,
            )
            self.controls.append(line)

        circle = ft.Container(
            ft.Text(node[0].capitalize(), size=self.text_size/1.5, color=ft.colors.BLACK),
            width=100,
            height=100,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=ft.border_radius.all(25),
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=0, bottom=0),
            on_click=lambda _: webbrowser.open_new_tab(node[1]),
        )
        self.controls.append(circle)

        self.update()

    def clear(self):
        self.controls = []
        self.update()

    def set_path(self, nodes):
        self.controls = []
        for index, node in enumerate(nodes):
            circle = ft.Container(
                ft.Text(node, size=self.text_size, color=ft.colors.BLACK),
                width=100,
                height=100,
                bgcolor=ft.colors.WHITE,
                border=ft.border.all(1, ft.colors.BLACK),
                border_radius=ft.border_radius.all(25),
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=0, bottom=0),
            )
            self.controls.append(circle)
            self.update()
            time.sleep(0.5)

            if index < len(nodes) - 1:
                line = ft.Container(
                    width=2,
                    height=60,
                    margin=ft.margin.only(left=50, top=0, bottom=0),
                    bgcolor=ft.colors.WHITE,
                )
                self.controls.append(line)
        self.update()
