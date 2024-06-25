import time
import webbrowser

import flet as ft

from crawler.WikiParser import WikiParser


class PathVisualisation(ft.Column):

    """
    A visual representation of paths through nodes in a graphical format. Each node represents a page or step
    in the path, and nodes are interconnected by lines to show their sequence.

    Extends:
        ft.Column: Inherits from Flet's Column class, which arranges its children in a vertical sequence.
    """
    def __init__(self):
        super().__init__()

        self.text_size = 20
        self.alignment = ft.MainAxisAlignment.CENTER
        self.spacing = 0
        self.width = 200
        self.scroll = ft.ScrollMode.ALWAYS

    def add_node(self, node: tuple[str, str], to_paint: bool = True):
        """
        Adds a visual node to the path visualization. Each node is clickable and opens the associated URL in a new tab.

        Args:
            node (tuple[str, str]): A tuple containing the display text and the URL of the node.
            to_paint (bool): If True, adds a line before the node to connect it to the previous node in the visualisation.
        """
        if to_paint:
            line = ft.Container(
                width=2,
                height=60,
                margin=ft.margin.only(left=50, top=0, bottom=0),
                bgcolor=ft.colors.WHITE,
            )
            self.controls.append(line)

        circle = ft.Container(
            ft.Text(WikiParser.get_wiki_url_name(node[1]), size=self.text_size/1.5, color=ft.colors.BLACK),
            width=100,
            height=100,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=ft.border_radius.all(25),
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=0, bottom=0),
            on_click=lambda _: webbrowser.open_new_tab(node[1]),
            padding=ft.padding.all(2),
        )
        self.controls.append(circle)

        self.update()

    def clear(self):
        self.controls = []
        self.update()

    def set_path(self, nodes):
        """
        Sequentially displays a list of nodes as a visual path. This method adds each node to the visualization
        with a delay, simulating the path being built progressively.

        Args:
            nodes (list): A list of nodes (strings) to visualize.
        """
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
