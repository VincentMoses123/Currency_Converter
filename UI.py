import Currency_Converter

from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static




class get_currencies(Static):
    "Currencies"

class main(Static):
    """A CC widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets of a Converter."""
        yield Button("List", id="start", variant="success")
        yield Button("Convert", id="stop", variant="error")
        yield Button("Rate", id="reset")
        yield Button("Quit")

class Currency_Converter(App):
    """My Currency Converter UI"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def main(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(main(), main(), main())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = Currency_Converter()
    app.run()