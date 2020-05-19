class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def __repr__(self):
        return str(self.data)
        

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        newnode = Node(item)
        newnode.setNext(self.head)
        self.head = newnode

    def size(self):
        current = self.head
        count = 0
        while current != None:  # or just while current:
            count += 1
            current = current.getNext()
        return count

    # for remove, both the current and previous nodes need to be tracked
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        # while current != None and not found:
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def __repr__(self):
        out = ""
        curnode = self.head
        while curnode:
            out += str(curnode.getData()) + " "
            curnode = curnode.next
        return out

def test():
    pass
