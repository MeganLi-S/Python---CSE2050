import unittest
from MyBSTMap import MyBSTMap

class TestMyBSTMap(unittest.TestCase):
    def testequal(self):
        t1 = MyBSTMap()
        t2 = MyBSTMap()
        self.assertEqual(t1,t2)
        t1.put(7, "seven")
        self.assertNotEqual(t1,t2)
        t2.put(7, "seven")
        self.assertEqual(t1,t2)
        for i in [9,5,2,1,4,3,6]:
            t1.put(i, 2*i)
        for i in [5,2,4,1,9,3]:
            t2.put(i, 2*i)
        self.assertNotEqual(t1,t2)
        t2.put(6,12)
        self.assertEqual(t1,t2)


    def testfrompreorder(self):
        keys = [3,1,0,2]
        t = MyBSTMap.frompreorder([(k,k) for k in keys])
        self.assertEqual(t.root.key, 3)
        self.assertEqual(t.root.left.key, 1)
        self.assertEqual(t.root.left.left.key, 0)
        self.assertEqual(t.root.left.right.key, 2)

    def testfrompostorder(self):
        keys = [3,1,0,2]
        t = MyBSTMap.frompostorder([(k,k) for k in keys])
        self.assertEqual(t.root.key, 2)
        self.assertEqual(t.root.left.key, 0)
        self.assertEqual(t.root.right.key, 3)
        self.assertEqual(t.root.left.right.key, 1)

    def testfrompreorder_largeinstance(self):
        t1 = MyBSTMap()
        for i in range(1000):
            t1.put(i * 382371 % 1001)
        t2 = MyBSTMap.frompreorder(list(t1.preorder()))
        self.assertEqual(t1, t2)
        t2.put(-1)
        self.assertNotEqual(t1,t2)

    def testfrompostorder_largeinstance(self):
        t1 = MyBSTMap()
        for i in range(1000):
            t1.put(i * 382371 % 1001)
        t2 = MyBSTMap.frompostorder(list(t1.postorder()))
        self.assertEqual(t1, t2)
        t2.put(-1)
        self.assertNotEqual(t1,t2)

if __name__ == '__main__':
    unittest.main()
