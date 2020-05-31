import unittest
from point import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1,2,3)
    
    def test_string_representation(self):
        point = Point(1, 2, 3)
        self.assertEqual(str(point), 'Point(x=1, y=2, z=3)')
        self.assertEqual(repr(point), 'Point(x=1, y=2, z=3)')
        point.y = 4
        self.assertEqual(str(point), 'Point(x=1, y=4, z=3)')
        self.assertEqual(repr(point), 'Point(x=1, y=4, z=3)')

    def test_equality_and_inequality(self):
        p1 = Point(1, 2, 3)
        p2 = Point(1, 2, 4)
        p3 = Point(1, 2, 3)
        self.assertNotEqual(Point(1, 2, 3), Point(1, 2, 4))
        self.assertEqual(Point(1, 2, 3), Point(1, 2, 3))
        self.assertFalse(Point(1, 2, 3) != Point(1, 2, 3))
        self.assertNotEqual(p1, p2)
        self.assertEqual(p1, p3)
        p3.x, p3.z = p3.z, p3.x
        self.assertNotEqual(p1, p3)
        self.assertTrue(p1 != p3)
        self.assertFalse(p1 == p3)



    def test_init(self):
        p2 = Point(x=1, y=2, z=3)
        self.assertEqual(self.p1, p2)
    
    def test_mutate(self):
        self.p1.x = 4
        self.assertEqual(self.p1, Point(4, 2, 3))

    def test_bonus1(self):
        p2 = Point(4,5,6)
        self.assertEqual(self.p1+p2, Point(5,7,9))
        self.assertEqual(p2 - self.p1, Point(3,3,3))
    
    def test_bonus2(self):
        self.assertEqual( self.p1 * 2, Point(2,4,6))


    def test_bonus3(self):
        x,y,z = self.p1
        self.assertEqual(x,1)
        self.assertEqual(y,2)
        self.assertEqual(z,3)
    
if __name__ == '__main__':
    unittest.main()