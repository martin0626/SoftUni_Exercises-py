from project.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name=name, type="Power", capacity=int(capacity * 0.25), memory=int(memory + memory * 0.75))
