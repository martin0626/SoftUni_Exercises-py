from project.library import Library
from project.user import User
import unittest

class TestsUser(unittest.TestCase):
    def setUp(self):
        self.user = User(12, 'Valentina')
        self.library = Library()

    def test_info_method_should_return_sorted_books_list(self):
        self.library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosophers Stone',
                                                        'Harry Potter and the Deathly Hallows',
                                                        'Harry Potter and the Order of the Phoenix']})
        self.user.get_book('J.K.Rowling', 'Harry Potter and the Order of the Phoenix', 3, self.library)
        self.user.get_book('J.K.Rowling', 'Harry Potter and the Philosophers Stone', 3, self.library)
        self.user.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 3, self.library)

        result = self.user.info()
        self.assertEqual(result, "Harry Potter and the Deathly Hallows, Harry Potter and the Order of the Phoenix, Harry Potter and the Philosophers Stone")


if __name__ == "__main__":
    unittest.main()
