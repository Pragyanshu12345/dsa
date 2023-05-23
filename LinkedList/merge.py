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

    def merge(self, ll, ll1, mergedlist):
        # 1-->5-->9  2-->4-->6   1-->2-->4-->5--
        currfirst = ll.head
        currsecond = ll1.head
        while (True):
            if (currfirst == None):
                mergedlist.insert(currsecond)
                break
            if (currsecond == None):
                mergedlist.insert(currfirst)
                break
            if (currfirst.data < currsecond.data):
                currfirstnext = currfirst.next
                currfirst.next = None
                mergedlist.insert(currfirst)
                currfirst= currfirstnext
            else:
                currsecondnext = currsecond.next
                currsecond.next = None
                mergedlist.insert(currsecond)
                currsecond = currsecondnext

    def printll(self):
        currentnode = self.head
        if (self.head == None):
            print("List is Empty")
        while True:
            if (currentnode is None):
                break
            print(currentnode.data)
            currentnode = currentnode.next


nodeone = Node(1)
nodefive = Node(5)
nodenine = Node(9)
nodetwelve=Node(12)
ll = LinkedList()
ll.insert(nodeone)
ll.insert(nodefive)
ll.insert(nodenine)
ll.insert(nodetwelve)

nodetwo = Node(2)
nodefour = Node(4)
nodesix = Node(6)
ll1 = LinkedList()
ll1.insert(nodetwo)
ll1.insert(nodefour)
ll1.insert(nodesix)

mergedlist = LinkedList()
mergedlist.merge(ll, ll1, mergedlist)
mergedlist.printll()
