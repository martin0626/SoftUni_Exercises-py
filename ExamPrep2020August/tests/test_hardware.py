from unittest import TestCase, main
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):

    def setUp(self):
        self.hardware = Hardware('ASD', 'HDD', 100, 10)

    def test_constructor__init_method(self):
        self.assertEqual('ASD', self.hardware.name)
        self.assertEqual('HDD', self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(10, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)
        # self.assertEqual(0, self.hardware.used_memory)
        # self.assertEqual(0, self.hardware.used_capacity)

    def test_install_software_with_enough_memory__capacity(self):
        software = Software('Linux', 'Light', 1, 1)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_install_software_without_enough_memory__capacity(self):
        software = Software('Linux', 'Light', 100, 100)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual('Software cannot be installed', str(ex.exception))
        self.assertEqual(0, len(self.hardware.software_components))

    def test_uninstall__method(self):
        software = Software('Linux', 'Light', 1, 1)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))


if __name__ == "__main__":
    main()
