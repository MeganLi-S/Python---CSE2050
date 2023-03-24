from BSTMap import BSTMap, BSTNode # provided for you

class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use the correct Node class

    # TODO: implement the three methods below
    def __eq__(self, other):
        return MyBSTNode.__eq__(self.root, other.root)#(Note that this method exists in MyBSTNode - this one should call that one)

    # the below is a "static" method
    # it belongs to the class, but does not take an instance of this class (self) as a parameter
    # note the "decorator" @staticmethod - this let's python know this is not a typical method
    @staticmethod
    def frompreorder(L):
        My_Map = BSTMap()
        for i in L:
            My_Map.put(i[0], i[1])

        return My_Map
        

    @staticmethod
    def frompostorder(L):
        L = reversed(L)
        My_Map = BSTMap()
        for i in L:
            My_Map.put(i[0], i[1])

        return My_Map

class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        if self is None or other is None:
            if self is None and other is None:
                return True
            else:
                return False
        else:
            return self.left == other.left and self.right == other.right
            
            

t1 = MyBSTMap()
t2 = MyBSTMap()
print(t1)
print(t2)
assert t1 == t2
t1.put(7, "seven")
assert t1 != t2
t2.put(7, "seven")
assert t1 == t2
for i in [9,5,2,1,4,3,6]:
    t1.put(i, 2*i)
for i in [5,2,4,1,9,3]:
    t2.put(i, 2*i)
print("hello!")
assert t1 != t2
t2.put(6,12)
assert t1 == t2

keys = [3,1,0,2]
t = MyBSTMap.frompreorder([(k,k) for k in keys])
assert t.root.key == 3
# self.assertEqual(t.root.left.key, 1)
# self.assertEqual(t.root.left.left.key, 0)
# self.assertEqual(t.root.left.right.key, 2)

t1 = MyBSTMap()
for i in range(1000):
    t1.put(i * 382371 % 1001)
t2 = MyBSTMap.frompostorder(list(t1.postorder()))
assert t1 == t2
# t2.put(-1)
# self.assertNotEqual(t1,t2)    