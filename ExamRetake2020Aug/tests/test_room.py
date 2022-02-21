from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.people.child import Child
from unittest import TestCase, main


class TestRoom(TestCase):

    def setUp(self):
        self.room = Room('Ivanov', 1000, 2)

    def test_init_method(self):
        self.assertEqual('Ivanov', self.room.family_name)
        self.assertEqual(1000, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual(0, len(self.room.children))
        self.assertEqual(0, self.room._expenses)

    def test__expenses_property_with_valid_value(self):
        self.room.expenses = 10
        self.assertEqual(10, self.room.expenses)

    def test_add_child(self):
        self.room.children.append(Child(1, 2, 3, 4, 5))
        self.assertEqual(1, len(self.room.children))

    def test__expenses_attribute_with_valid_value(self):
        self.room.expenses = 10
        self.assertEqual(10, self.room._expenses)

    def test__expenses_property(self):
        self.assertEqual(0, self.room.expenses)

    def test__expenses_property_with_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -111
        self.assertEqual('Expenses cannot be negative', str(ex.exception))

    def test__calculate_expenses_method_set_property(self):
        fridge = Fridge()
        child = Child(1, 2, 3, 4)
        self.room.calculate_expenses(fridge, child)
        expected = fridge.get_monthly_expense() + child.get_monthly_expense()
        self.assertEqual(expected, self.room.expenses)

    def test__calculate_expenses_method(self):
        self.assertEqual(self.room.expenses, self.room._expenses)


if __name__ == '__main__':
    main()
