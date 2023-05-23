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

    def length(self):
        currnode, y = self.head, 0
        while (currnode is not None):
            y += 1
            currnode = currnode.next
        return y

    def insertathead(self, newNode):
        if (self.head == None):
            self.head = newNode
        else:
            tempnode = self.head
            self.head = newNode
            self.head.next = tempnode

    def insertinbetween(self, newNode, i):
        if (self.head == None):
            self.head = newNode
        if (i < 0 or i > self.length()):
            print("Invalid index")
            return
        if (i == 0):
            self.insertathead(newNode)
            return
        currnode = self.head
        prevnode = self.head
        y = 0
        while (True):
            if (i == y):
                prevnode.next = newNode
                newNode.next = currnode
                break
            y += 1
            prevnode = currnode
            currnode = currnode.next

    def delete1(self, pos):
        if (pos < 0 or pos >= self.length()):
            print("Invalid position")
            return
        if (pos == 0):
            currnode = self.head
            self.head = currnode.next
            del currnode
            return
        currnode = prevnode = self.head
        y = 0
        while (True):
            if (pos == y):
                if currnode.next is not None:  # Check that currnode.next is not None
                    prevnode.next = currnode.next
                else:
                    prevnode.next = None
                # del currnode
                break
            prevnode = currnode
            currnode = currnode.next
            y += 1

    def printll(self):
        currentnode = self.head
        if (self.head == None):
            print("List is Empty")
        while True:
            if (currentnode is None):
                break
            print(currentnode.data)
            currentnode = currentnode.next


firstnode = Node("Pragya")
ll = LinkedList()
ll.insert(firstnode)
secondnode = Node("Shubrah")
ll.insert(secondnode)
thirdnode = Node("Nishant")
ll.insert(thirdnode)
fourthnode = Node("Yashika")
ll.insert(fourthnode)
fifthnode = Node("Akshay")
ll.insertinbetween(fifthnode, 2)
ll.delete1(5)
ll.length()
ll.printll()
print(ll.length())
