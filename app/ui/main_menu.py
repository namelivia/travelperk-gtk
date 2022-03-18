from gi.repository import Gtk
import gi
from .cost_center import CreateCostCenterBox
from .greenperk import GreenPerkBox
gi.require_version("Gtk", "3.0")


class CreateMainMenuBox:

    def __init__(self, window):
        self.box = self._create_box()
        self.window = window
        self._create_cost_center_button(self.box)
        self._create_greenperk_button(self.box)

    def _create_box(self):
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        box.set_border_width(10)
        box.set_spacing(6)
        return box

    def _create_cost_center_button(self, box):
        cost_center_button = Gtk.Button("Create a Cost Center")
        cost_center_button.connect('clicked', self._create_cost_center_box)
        box.add(cost_center_button)

    def _create_greenperk_button(self, box):
        greenperk_button = Gtk.Button("GreenPerk")
        greenperk_button.connect('clicked', self._create_greenperk_box)
        box.add(greenperk_button)

    def _create_window(self, name):
        window = Gtk.Window()
        window.set_title(name)
        window.set_position(Gtk.WindowPosition.CENTER)
        return window

    def _create_greenperk_box(self, ref):
        window = self._create_window("GreenPerk")
        window.add(GreenPerkBox(window).get())
        window.show_all()

    def _create_cost_center_box(self, ref):
        window = self._create_window("Create a Cost Center")
        window.add(CreateCostCenterBox(window).get())
        window.show_all()

    def get(self):
        return self.box
