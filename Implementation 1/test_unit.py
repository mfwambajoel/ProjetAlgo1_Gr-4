import unittest
from implementation1_module import*

class Test(unittest.TestCase):
    def test_surface(self):
        self.assertEqual(Rectangle(8,9).surface(),72)
        self.assertEqual(Carre(4).surface(),16)
        self.assertEqual(Cercle(9).surface(),254.46900494077323)
        self.assertEqual(TriRectangle(4,9).surface(),18)

    def test_perimeter(self):
        self.assertEqual(Rectangle(5,9).perimeter(),28)
        self.assertEqual(Carre(5).perimeter(),20)
        self.assertEqual(Triangle(5,8,6).perimeter(),19)
        self.assertEqual(Cercle(5).perimeter(),31.41592653589793)


if __name__=='__main__':
    unittest.main()