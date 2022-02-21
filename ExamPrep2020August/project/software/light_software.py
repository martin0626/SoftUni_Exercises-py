from project.software.software import Software


class LightSoftware(Software):

    def __init__(self, name, capacity_consumption, memory_consumption):
        self.__consumption_add = capacity_consumption * 0.5
        self.__memory_decrease = memory_consumption * 0.5
        super().__init__(name=name, type='Light', capacity_consumption=int(capacity_consumption + self.__consumption_add),
                         memory_consumption=int(memory_consumption - self.__memory_decrease))


