from node import ListNode as Node
from structure import Structure


class SinglyLinkedList(Structure):
    ''' Class that define a singly linked list '''

    def __init__(self):
        super().__init__()

    def append(self, data):
        node = Node(data)

        if self._tail == None:
            self._front = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

        self._size+=1

    def delete(self,data):
        current = self._front
        __next = self._front

        while current.next:
            if current.next.data == data:
                if current.next == self._tail:
                    current.next = None
                else:
                    _prev = current
                    __next = current.next.next
                    _prev.next = __next

                self._size-=1
                return True
            else:
                current = current.next

        return False

    def insert(self, data , next_to):
        current = self.search(next_to)

        if current:
            new_node = Node(data)

            if current == self._tail:
                current.next = new_node
            else:
                new_node.next = current.next
                current.next = new_node

            self._size += 1
        else:
            raise ValueError("Positional element is not in the list")

    def search(self,data):
        current = self._front

        while current:
            if current.data == data:
                return current
            else:
                current = current.next

        return False