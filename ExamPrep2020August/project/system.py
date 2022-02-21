from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware_instance = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware_instance)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hr_instance = HeavyHardware(name, capacity, memory)
        System._hardware.append(hr_instance)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        es_instance = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware = [h for h in System._hardware if h.name == hardware_name]

        if hardware:
            try:
                hardware[0].install(es_instance)
                System._software.append(es_instance)
                return
            except Exception as message:
                return str(message)

        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        ls_instance = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware = [h for h in System._hardware if h.name == hardware_name]

        if hardware:
            try:
                hardware[0].install(ls_instance)
                System._software.append(ls_instance)
                return

            except Exception as message:
                return str(message)
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]
        if not hardware:
            return 'Some of the components do not exist'

        elif not software:
            return 'Some of the components do not exist'

        if software[0] not in hardware[0].software_components:
            return 'Some of the components do not exist'

        hardware[0].uninstall(software[0])
        System._software.remove(software[0])

    @staticmethod
    def analyze():
        total_memory = sum([h.memory for h in System._hardware])
        memory_use = sum([h.used_memory for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])
        capacity_use = sum([h.used_capacity for h in System._hardware])
        return f"System Analysis" \
               f"\nHardware Components: {len(System._hardware)}" \
               f"\nSoftware Components: {len(System._software)}" \
               f"\nTotal Operational Memory: {memory_use:g} / {total_memory:g}" \
               f"\nTotal Capacity Taken: {capacity_use:g} / {total_capacity:g}"

    @staticmethod
    def system_split():

        result = ''

        for hardware in System._hardware:
            ep_software = len([s for s in hardware.software_components if s.__class__.__name__ == "ExpressSoftware"])
            ls_software = len([s for s in hardware.software_components if s.__class__.__name__ == "LightSoftware"])
            names_software = [s for s in hardware.software_components]

            if names_software:
                names_software = ', '.join([s.name for s in hardware.software_components])
            else:
                names_software = None

            result += f'Hardware Component - {hardware.name}' \
                    f'\nExpress Software Components: {ep_software}' \
                    f'\nLight Software Components: {ls_software}' \
                    f'\nMemory Usage: {hardware.used_memory:g} / {hardware.memory:g}' \
                    f'\nCapacity Usage: {hardware.used_capacity:g} / {hardware.capacity:g}' \
                    f'\nType: {hardware.type}' \
                    f'\nSoftware Components: {names_software}\n'
        return result

