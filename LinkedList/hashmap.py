class Node:
    def __init__(self, value, next_node=None):
        self.val = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def insert(self, val):
        if val not in self:
            new_node = Node(val, self.head.next)
            self.head.next = new_node

    def remove(self, val):
        curr = self.head
        while curr.next != None:
            if val == curr.next.val:
                curr.next = curr.next.next
                return
            curr = curr.next

    def __contains__(self, val):
        curr = self.head.next
        while curr is not None:
            if curr.val == val:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False


class MyHashSet(object):

    def __init__(self):
        self.size = 721
        self.buckets = [LinkedList() for i in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.buckets[self._hash(key)].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.buckets[self._hash(key)].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.buckets[self._hash(key)]
