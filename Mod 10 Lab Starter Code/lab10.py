class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        return False

    
        

class PQ_UL:
    def __init__(self):
        self._PQ = []
        self._len = 0

    def __eq__(self, other):
        if other is None:
            return False
        elif self._len != other._len:
            return False
        else:
            boolean = True
            for i in range(self._len):
                if self._PQ[i] != other._PQ[i]:
                    boolean = False
            return boolean

    def __len__(self):
        return self._len
    
    def insert(self, item, priority):
        new_entry = Entry(item, priority)
        self._PQ.append(new_entry)
        self._len += 1
        return
  

    def find_min(self):
        min = self._PQ[0].priority
        min_item = self._PQ[0].item
        for i in self._PQ:
            if i.priority < min:
                min_item = i.item
                min = i.priority

        return min_item
            

    def remove_min(self):
        min = self._PQ[0].priority
        min_item = self._PQ[0].item
        for i in self._PQ:
            if i.priority < min:
                min_item = i.item
                min = i.priority
                
        return self._PQ.pop(min)


class PQ_OL:
    def __init__(self):
        self._PQ = []
        self._len = 0

    def __len__(self):
        return self._len
    
    def insert(self, item, priority):
        self._PQ.append(Entry(item, priority))
        self._PQ.sort(reverse = True)

    def find_min(self):
        return self._PQ[-1].item

    def remove_min(self):
        return self._PQ.pop().item


pq = PQ_UL()
n = 100
for i in range(n):
    assert len(pq) == i
    pq.insert(str(i), i)
old = pq.remove_min()

for i in range(1, n):
    peak = pq.find_min()
    new = pq.remove_min()
    assert new == peak
    assert old.priority <= new.priority
    assert len(pq) == n - i - 1
    old = new