from gi.repository import Gtk
from ui.main_menu import CreateMainMenuBox
import gi
gi.require_version("Gtk", "3.0")


class TravelPerk:
    def _create_window(self):
        window = Gtk.Window()
        window.set_title(
            "TravelPerk"
        )
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect("destroy", Gtk.main_quit)
        return window

    def main(self):
        window = self._create_window()
        window.add(CreateMainMenuBox(window).get())
        window.show_all()
        Gtk.main()


if __name__ == "__main__":
    TravelPerk().main()
