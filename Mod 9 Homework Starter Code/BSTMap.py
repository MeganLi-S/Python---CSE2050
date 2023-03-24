# You don't need to modify this file
# It is general BST starter code
class BSTMap:
    def __init__(self):
        self.root = None

    def newnode(self, key, value = None):
        return BSTNode(key, value)

    def get(self, key):
        if self.root is None:
            raise KeyError
        node = self.root.get(key)
        return node.value

    def put(self, key, value = None):
        if self.root is None:
            self.root = self.newnode(key, value)
        else:
            self.root = self.root.put(key, value)

    def remove(self, key):
        if self.root is not None:
            self.root = self.root.remove(key)

    def preorder(self):
        for n in self.root._preorder():
            yield (n.key, n.value)

    def postorder(self):
        for n in self.root._postorder():
            yield (n.key, n.value)

    def __str__(self):
        return str(self.root)

class BSTNode:
    newnode = BSTMap.newnode

    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def get(self, key):
        if key == self.key:
            return self
        if key < self.key and self.left is not None:
            return self.left.get(key)
        if key > self.key and self.right is not None:
            return self.right.get(key)
        raise KeyError

    def put(self, key, value = None):
        if key == self.key:
            self.value = value
        if key < self.key:
            if self.left is None: self.left = self.newnode(key,value)
            else: self.left = self.left.put(key, value)
        if key > self.key:
            if self.right is None: self.right = self.newnode(key,value)
            else: self.right = self.right.put(key, value)
        return self

    def rotateright(self):
        newroot = self.left
        self.left = newroot.right
        newroot.right = self
        return newroot

    def rotateleft(self):
        newroot = self.right
        self.right = newroot.left
        newroot.left = self
        return newroot

    def _remove(self):
        if self.left is None and self.right is None:
            return None
        if self.left is not None:
            newroot = self.rotateright()
            newroot.right = self._remove()
            return newroot
        else:
            newroot = self.rotateleft()
            newroot.left = self._remove()
            return newroot

    def remove(self, key):
        if key == self.key:
            return self._remove()
        if key < self.key and self.left is not None:
            self.left = self.left.remove(key)
            return self
        if key > self.key and self.right is not None:
            self.right = self.right.remove(key)
            return self
        raise KeyError

    def tostring(self, level = 0):
        s = [("--" * level) + str(self.key)]
        for c in [n for n in (self.left, self.right) if n]:
            s.append(c.tostring(level + 1))
        return "\n".join(s)

    def __str__(self):
        return self.tostring()

    def _preorder(self):
        yield self
        if self.left:
            for n in self.left._preorder():
                yield n
        if self.right:
            for n in self.right._preorder():
                yield n

    def _postorder(self):
        if self.left:
            for n in self.left._postorder():
                yield n
        if self.right:
            for n in self.right._postorder():
                yield n
        yield self
