from gi.repository import Gtk
from backend.travelperk import get_backend
import gi
gi.require_version("Gtk", "3.0")


class GreenPerkBox:

    def __init__(self, window):
        self.box = self._create_box()
        self.window = window
        self._create_origin_label(self.box)
        self._create_origin_input(self.box)
        self._create_destination_label(self.box)
        self._create_destination_input(self.box)
        self._create_cabin_class_label(self.box)
        self._create_cabin_class_input(self.box)
        self._create_airline_code_label(self.box)
        self._create_airline_code_input(self.box)
        self._create_query_button(self.box)

    def calculate_emissions(self, ref):
        origin = self.origin_input.get_text()
        destination = self.destination_input.get_text()
        cabin_class = self.cabin_class_input.get_text()
        airline_code = self.airline_code_input.get_text()
        try:
            emissions = get_backend().greenperk().greenperk().flight_emissions(
              origin,
              destination,
              cabin_class,
              airline_code
            )
            dialog = Gtk.MessageDialog(
                transient_for=self.window,
                flags=0,
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                text=f"The distance is {emissions.distance_km} mk. Emission: {emissions.emissions.CO2e_kg} CO2e/kg",
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

    def _create_origin_label(self, box):
        serial_label = Gtk.Label()
        serial_label.set_text('Origin')
        box.add(serial_label)

    def _create_origin_input(self, box):
        self.origin_input = Gtk.Entry()
        self.origin_input.props.xalign = 0.5
        box.add(self.origin_input)

    def _create_destination_label(self, box):
        serial_label = Gtk.Label()
        serial_label.set_text('Destination')
        box.add(serial_label)

    def _create_destination_input(self, box):
        self.destination_input = Gtk.Entry()
        self.destination_input.props.xalign = 0.5
        box.add(self.destination_input)

    def _create_cabin_class_label(self, box):
        serial_label = Gtk.Label()
        serial_label.set_text('Cabin class')
        box.add(serial_label)

    def _create_cabin_class_input(self, box):
        self.cabin_class_input = Gtk.Entry()
        self.cabin_class_input.props.xalign = 0.5
        box.add(self.cabin_class_input)

    def _create_airline_code_label(self, box):
        serial_label = Gtk.Label()
        serial_label.set_text('Airline code')
        box.add(serial_label)

    def _create_airline_code_input(self, box):
        self.airline_code_input = Gtk.Entry()
        self.airline_code_input.props.xalign = 0.5
        box.add(self.airline_code_input)

    def _create_query_button(self, box):
        query_button = Gtk.Button("Calculate emissions")
        query_button.connect('clicked', self.calculate_emissions)
        box.add(query_button)

    def get(self):
        return self.box
