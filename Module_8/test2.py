import unittest
import main

class Test(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(main.discriminant(12, 333, 21), 109881)

    def test_solv_square(self):
        self.assertEqual(main.solv_square(12, 333, 21), (-0.06320703167036375, -27.686792968329637))

    def test_roots(self):
        self.assertEqual(main.roots(109881, 12, 333, 21), (-0.06320703167036375, -27.686792968329637))

    def test_roots2(self):
        self.assertEqual(main.roots(0, 1, -6, 9), (3))

    def test_roots3(self):
        self.assertEqual(main.roots(-131, 5, 3, 7), (None))

unittest.main()
