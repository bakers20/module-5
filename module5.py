import unittest
from myapp.models import Book  # Assuming the model is defined in myapp/models.py
from myapp import create_book, get_book_by_id, update_book, delete_book  # Your CRUD functions

class TestBookAPI(unittest.TestCase):
    def setUp(self):
        """Setup for testing: run before each test."""
        # Create a sample book for testing
        self.book = create_book('Test Book', 'Test Author', 'Test Publisher')

    def tearDown(self):
        """Cleanup after testing: run after each test."""
        delete_book(self.book.id)

    def test_create_book(self):
        """Test if a book is created successfully."""
        book = create_book('Another Book', 'Another Author', 'Another Publisher')
        self.assertIsNotNone(book.id)
        self.assertEqual(book.book_name, 'Another Book')

    def test_get_book(self):
        """Test retrieving a book by its ID."""
        retrieved_book = get_book_by_id(self.book.id)
        self.assertEqual(retrieved_book.book_name, self.book.book_name)

    def test_update_book(self):
        """Test updating a book's details."""
        updated_book = update_book(self.book.id, 'Updated Name', 'Updated Author', 'Updated Publisher')
        self.assertEqual(updated_book.book_name, 'Updated Name')

    def test_delete_book(self):
        """Test deleting a book."""
        delete_book(self.book.id)
        retrieved_book = get_book_by_id(self.book.id)
        self.assertIsNone(retrieved_book)

if __name__ == '__main__':
    unittest.main()


# The test results mean that the code is running and functioning correctly and no assertion failed. If it does run corrently, it will say OK and give the amount of time it takes to test it.