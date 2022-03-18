from gi.repository import Gtk
from backend.travelperk import get_backend
import gi
gi.require_version("Gtk", "3.0")


class CreateCostCenterBox:

    def __init__(self, window):
        self.box = self._create_box()
        self.window = window
        self._create_cost_center_label(self.box)
        self._create_cost_center_input(self.box)
        self._create_create_button(self.box)

    def create_cost_center(self, ref):
        name = self.cost_center_input.get_text()
        try:
            cost_center = get_backend().cost_centers().cost_centers().create(name)
            dialog = Gtk.MessageDialog(
                transient_for=self.window,
                flags=0,
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                text=f"The new cost center {cost_center.name} has been sucessfully created",
            )
            dialog.run()
            dialog.destroy()
        except Exception as e:
            dialog = Gtk.MessageDialog(
                transient_for=self.window,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.CANCEL,
                text="Error creating cost center",
            )
            dialog.format_secondary_text(str(e))
            dialog.run()
            dialog.destroy()

    def _create_box(self):
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        box.set_border_width(10)
        box.set_spacing(6)
        return box

    def _create_cost_center_label(self, box):
        serial_label = Gtk.Label()
        serial_label.set_text('Name')
        box.add(serial_label)

    def _create_cost_center_input(self, box):
        self.cost_center_input = Gtk.Entry()
        self.cost_center_input.props.xalign = 0.5
        box.add(self.cost_center_input)

    def _create_create_button(self, box):
        create_button = Gtk.Button("Create")
        create_button.connect('clicked', self.create_cost_center)
        box.add(create_button)

    def get(self):
        return self.box
