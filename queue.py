from node import QueueNode as Node
from structure import Structure

class Queue(Structure):

    def __init__(self):
        super().__init__()

    def push_back(self, data):
        '''Inserts a new element at the endo fo the queue'''
        node = Node(data)

        #if the tail is None it means that the queue is empty and
        #this piece of code make the first element of the list
        if self._tail == None:
            self._front = node
            self._tail = node
        #if the tail is not None it means that the queue is not empty
        #and this piece of code make the last element of the list
        #so assign the tail to a new node and assign the new node waiting to be used
        else:
            self._tail.next = node
            self._tail = node

        self._size += 1

    #this piece of code is used for removes elements, as we know, the queue only
    #removes the first node that was inserted in the queue, so we pop the front only
    def pop_front(self):
        '''Removes the first element of the queue'''
        current = self._front
        if current.next == None:
            self._front = None
            self._tail = None
        else:
            self._front = current.next
            current.next = None

        self._size -= 1
