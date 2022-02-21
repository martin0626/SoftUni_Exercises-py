from project.software.software import Software


class Hardware:

    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.used_memory = 0
        self.used_capacity = 0

    def install(self, software):
        if (self.capacity - self.used_capacity) >= software.capacity_consumption and \
                (self.memory - self.used_memory) >= software.memory_consumption:
            self.software_components.append(software)
            self.used_memory += software.memory_consumption
            self.used_capacity += software.capacity_consumption
            return
        raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
            self.used_capacity -= software.capacity_consumption
            self.used_memory -= software.memory_consumption
