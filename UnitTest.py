from MathArea import MathShape
import unittest

class TestShapeLibrary(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self):
        self.library = MathShape()

    def test_calculate_circle_area(self):
        self.assertEqual(self.library.calculate_shape_area("Круг", radius=2), 12.566370614359172)
        self.assertRaises(KeyError, self.library.calculate_shape_area, "Треугольник", side1=2)

    def test_calculate_triangle_area(self):
        self.assertEqual(self.library.calculate_shape_area("Треугольник", side1=3, side2=4, side3=5), 6)
        self.assertRaises(KeyError, self.library.calculate_shape_area, "Треугольник", radius=4)
        self.assertRaises(ValueError, self.library.calculate_shape_area, "Прямоугольник", side1=4, side2=5)


if __name__ == '__main__':
    unittest.main()

