#import the DoubleLinkedList method from the doubleLinkedList.py file
from doubleLinkedList import DoubleLinkedList

#create a new instance of the DoubleLinkedList class
if __name__ == '__main__':
    t=""
    #make a variable with the method 
    my_list = DoubleLinkedList()

    #print the sieze and if the list is empty to check the list is empty
    print(f'List Size = {my_list.size()}')
    print(f'If list is empty =  {my_list.empty()}')
    print(t.center(50,'-'))
    #add a new item to the list
    my_list.append("Joshua")

    #function to don't repeat the results in the console
    #print the sieze, if the list is empty to check the list is empty and the first item in the list and the last
    def print_list(my_list):
        print(f'List Front = {my_list.front()}')
        print(f'List Back = {my_list.back()}')
        print(f'List Size = {my_list.size()}')
        print(f'If list is empty =  {my_list.empty()}')
        print(t.center(50,'-'))

    #append more items to the list
    my_list.append("Gustavo")
    my_list.append("Derek")
    my_list.append("Fabian")
    my_list.append("Fabian")
    my_list.append("David")
    my_list.append("Omar")
    my_list.append("Luis")
    my_list.append("Kevin")
    my_list.append("Jonathan")

    print_list(my_list)

    #use the iter function to show the list
    for name in my_list.iter():
        print(name)

    #use the delete function to delete an item from the list
    print(my_list.delete("Fabian"))

    #show the item fabian was deleted
    for name in my_list.iter():
        print(name)

    print_list(my_list)
    print(t.center(50,'-'))
    #use the search function to find an item in the list and show
    #in the console the item exists or not
    if my_list.search("Fabian"):
        element = my_list.search("Fabian")
        print(f'{element.data} exist in the list')
    else:
        print(False)

    print_list(my_list)

    #use the insert function to insert an item in the list in
    #a specific position and show in the console if it is succesful
    if (my_list.insert("Alex", "David") == True):
        print("Element inserted")

    #show the list after the insert if the connection between the nodes is correct
    #refering to prev nodes
    for name in my_list.reverse():
        print(name)

    print(t.center(50,'-'))

    #show the list normally to see if the connection between next nodes is correct
    for name in my_list.iter():
        print(name)

    print_list(my_list)
    #check in console with the function previous if the previous connection
    #with a node is correct
    print("The previous element of Omar is: " + my_list.previous("Omar").data)