#import ListDoubleNode from node.py and structure from structure.py
from node import ListDoubleNode as Node
from structure import Structure

#create a new instance of the DoubleLinkedList class with structure class
class DoubleLinkedList(Structure):
    ''' Class that define a double linked list '''

    def __init__(self):
        super().__init__()

    def append(self, data):
        node = Node(data)

        #if the tail is None it means that the list is empty and
        #this piece of code make the first element of the list
        if self._tail == None:
            self._front = node
            self._tail = node
        #if the tail is not None it means that the list is not empty
        #and this piece of code make the last element of the list
        #so assign the tail to the new node and assign the new node and linked the previous tail
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._size += 1

    def reverse(self):
        current = self._tail
        while current:
            data = current.data
            current = current.prev
            yield data

    def delete(self,data):
        current = self._front
        __next = self._front
        __prev = self._front

        #if the variable current is not None it means that the list is not empty
        #so it runs the while loop until the current is None
        while current:

            #if the current data is equal to the data that we want to delete
            #enter in the if statement
            if current.data == data:

                #it checks if the current is the tail of the list
                if current == self._tail:
                    #assign a variable previous node of the current node that we will delete
                    __prev = current.prev
                    #delete the connection between the previous node and the delete node
                    current.prev = None
                    #assign the None as the last node of the list
                    __prev.next = None
                    #reassign the tail to the previuos node of the deleted node
                    self._tail = __prev

                else:
                    #assign the connections of the previous node and next of the current node
                    #that we will delete as variuables
                    __next = current.next
                    __prev = current.prev
                    #delete the connections
                    current.next = None
                    current.prev = None

                    #assign the connections of the previous node and next of the previous node
                    __next.prev = __prev
                    __prev.next = __next

                self._size-=1
                return True

            #if the current data is not equal to the data that we want to delete
            #reassign the current to the next node
            else:
                current = current.next

        return False

    def insert(self, data , next_to):
        #search the node that we want to insert and if it exist, insert the data
        #next to the node that we refear
        current = self.search(next_to)

        if current:
            node = Node(data)
            #it checks if the current is the tail of the list
            if current == self._tail:
                #assign the connection of the data that we want to insert
                current.next = node
                #assign the tail as the new node
                self._tail = current.next
                #assign the connection of the new node with the previous node
                node.prev = current
            else:
                #assign the connection of the next node of the data that we want to insert
                node.next = current.next
                #assign the new position of the new node
                current.next = node
                #assign the connection of the new node with the previous node
                node.prev = current
                #assign the connection of the next node with the new node
                node.next.prev = node

            self._size += 1
            #return True if the node was inserted, only for show that in the console
            return True
        else:
            raise ValueError("Positional element is not in the list")

    def search(self,data):
        current = self._tail

        while current:
            if current.data == data:
                return current
            else:
                current = current.prev

        return False

    #this method is used to search and show the previous connection to authenticate the connection
    #of the node
    def previous(self,data):
        current = self._tail

        while current:
            if current.data == data:
                return current.prev
            else:
                current = current.prev

        return False