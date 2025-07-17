import unittest
from math_utils import add, divide

class TestMathUtils(unittest.TestCase):
    @unittest.skip("This test is skipped for demonstration.")
    def test_skip(self):
        self.assertEqual(add(1, 2), 3)

    @unittest.expectedFailure
    def test_expected_failure(self):
        # This will fail (deliberately)
        self.assertEqual(divide(5, 0), 0)
        
    def setUp(self):
        # Setup code can go here (if needed)
        pass

    def tearDown(self):
        # Teardown code can go here (if needed)
        pass

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 5.0)
        self.assertRaises(ValueError, divide, 10, 0)
        # Alternative way:
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main()
