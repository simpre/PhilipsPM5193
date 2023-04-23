import pyvisa as visa
import time


class PhilipsPM35193:
    inst = None

    signal_forms = {
        "sine": "WS",
        "triangle": "WT",
        "rect": "WQ"
    }

    voltage_types = {
        "Vpp": "LA",
        "Vrms": "LR",
        "dBm": "LL",
        "DCOffset": "V"
    }

    def __init__(self, port, resource_manager=visa.ResourceManager()):
        self.inst = resource_manager.open_resource(port)
        self.inst.write_termination = "\n"
        self.inst.read_termination = "\n"

    def set_frequency(self, frequency):
        cmd = "F {}".format(str(frequency))
        self.inst.write(cmd)

    def set_signalform(self, form):
        self.inst.write(self.signal_forms[form])

    def set_voltage(self, type, value):
        cmd = "{} {}".format(self.voltage_types[type], str(value))
        self.inst.write(cmd)


