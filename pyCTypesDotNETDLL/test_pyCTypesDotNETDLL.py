import unittest
import ctypes
import os

class TestDLL(unittest.TestCase):

    def setUp(self):
        """
        Load the DLL before each test. If the DLL can't be loaded, skip the test.
        """
        dll_path = '../DllExample/bin/x86/Debug/DllExample.dll'
        if not os.path.exists(dll_path):
            self.skipTest(f"DLL not found at {dll_path}. Build the C# project first.")

        try:
            self.lib = ctypes.cdll.LoadLibrary(dll_path)
        except OSError as e:
            self.fail(f"Failed to load DLL: {e}")

    def test_add_positive_numbers(self):
        """
        Test adding two positive numbers.
        """
        self.assertEqual(self.lib.add(3, 5), 8)

    def test_add_negative_numbers(self):
        """
        Test adding two negative numbers.
        """
        self.assertEqual(self.lib.add(-3, -5), -8)

    def test_add_mixed_numbers(self):
        """
        Test adding a positive and a negative number.
        """
        self.assertEqual(self.lib.add(3, -5), -2)

    def test_add_zero(self):
        """
        Test adding with zero.
        """
        self.assertEqual(self.lib.add(5, 0), 5)
        self.assertEqual(self.lib.add(0, 5), 5)

if __name__ == '__main__':
    unittest.main()
