import flet as ft

from ui.DialogWindow import DialogWindow
from ui.PathVisualisation import PathVisualisation
from crawler.CrawlerBase import CrawlerBase


class InputController(ft.Column):
    """
    Manages the input controls for specifying the source and target Wikipedia pages, and initiating
    the crawl process. This class handles user interactions and manages the visual feedback and
    error handling through associated dialog windows and visualization components.

    Extends:
           ft.Column: Inherits from Flet's Column class.

    Attributes:
        page (ft.Page): The Flet page context where this controller is being used.
        visualisationColumn (PathVisualisation): The visualization component where the crawl results are displayed.
        dialog (DialogWindow): The dialog window for showing messages and alerts.
    """
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
        self.slider = ft.Slider(min=2, max=400, value=2, width=320, height=40, divisions=398)
        self.sliderText = ft.Text("Depth: 2", size=self.text_size, width=120)

        def on_change(e):
            self.sliderText.value = f"Depth: {int(e.control.value)}"
            self.sliderText.update()

        self.slider.on_change = on_change
        self.sliderRow = ft.Row(
            [
                self.sliderText,
                self.slider,
            ],
        )

        self.searchButton = ft.ElevatedButton("Search", width=120, height=40, on_click=lambda _: self.search())

        self.border_radius = ft.border_radius.all(10)
        self.controls = [
            self.targetRow,
            self.sourceRow,
            self.sliderRow,
            self.searchButton,
        ]

    def search(self):
        """
        Initiates the search operation. Validates URLs, clears previous visualizations, handles the crawl process,
        and manages error and status messaging through the dialog window.
        """
        valid = self.validate_links(self.targetInput.value, self.sourceInput.value)

        if not valid:
            self.dialog.set_message("Invalid links")
            self.dialog.show()
            return

        self.visualisationColumn.clear()
        try:
            path = CrawlerBase().crawl(
                self.sourceInput.value,
                self.targetInput.value,
                int(self.slider.value),
                self.visualisationColumn.add_node
            )
        except Exception as e:
            self.dialog.set_message(str(e))
            self.dialog.show()
            self.visualisationColumn.clear()
            return


        if not path:
            self.dialog.set_message("Path not found")
            self.dialog.show()
            self.visualisationColumn.clear()
            return

        #self.visualisationColumn.set_path(path)



    def validate_links(self, target, source):
        """
           Validates the provided URLs to ensure they are in the expected format for Wikipedia.

           Args:
               target (str): The target Wikipedia URL.
               source (str): The source Wikipedia URL.

           Returns:
               bool: True if both URLs are valid Wikipedia URLs, False otherwise.
           """
        if not target or not source:
            return False

        if not target.startswith("https://en.wikipedia.org/wiki/") or not source.startswith("https://en.wikipedia.org/wiki/"):
            return False

        return True