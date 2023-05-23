class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if (self.head == None):
            self.head = newNode
        else:
            lastnode = self.head
            while (True):
                if (lastnode.next is None):
                    break
                lastnode = lastnode.next
            lastnode.next = newNode

    def reversell(self):
        p = self.head
        q = r = None
        while (p != None):
            r = q
            q = p
            p = p.next
            q.next = r
        self.head = q

    def printll(self):
        currentnode = self.head
        if (self.head == None):
            print("List is Empty")
        while True:
            if (currentnode is None):
                break
            print(currentnode.data)
            currentnode = currentnode.next


firstnode = Node("Nishant")
ll = LinkedList()
ll.insert(firstnode)
secondnode = Node("Shubrah")
ll.insert(secondnode)
thirdnode = Node("Pragya")
ll.insert(thirdnode)
fourthnode = Node("Yashika")
ll.insert(fourthnode)
fifthnode = Node("Abhay")
ll.insert(fifthnode)
ll.reversell()
ll.printll()
