from node import StackNode as Node
from structure import Structure

class Stack(Structure):
    #this data structure is for the stack, so we need to implement the push and pop methods
    #the difference is that it need to remove first the last element inserted in the stack
    #and we only can add nodes at the end of the stack
    def __init__(self):
        self._top = None
        self._size = 0

    #as I said, the stack only removes the last element inserted in the stack, so we need to
    # assign the top node when a new node is inserted in the stack
    def top(self):
        if self._top:
            return self._top.data
        else:
            return "None"

    #clear method is used to remove all the nodes of the stack
    def clear(self):
        self._top = None
        self._size = 0

    #this funtion separate and show the data of the stack in order of the top to the bottom
    def iter(self):
        current = self._top
        while current:
            data = current.data
            current = current.prev
            yield data

    #insterts a node like it is literally a stack, it pushs the nodes to added, for check the data of
    #the node, you nedd to pass over all the pushed nodes

    def push(self, data):
        node = Node(data)

        if self._top == None:
            self._top = node
        else:
            node.prev = self._top
            self._top = node

        self._size += 1

    #this method removes the last node inserted in the stack, and assign the top node to the previous top node
    def pop(self):
        if self._top == None:
            return "None"
        else:
            self._top = self._top.prev
            self._size -= 1
        return self._top