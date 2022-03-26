#import the Queue method from the queue.py file
from queue import Queue as Q

#create a new instance of the queue class
if __name__ == '__main__':
    t=""
    #make a variable with the method
    my_q = Q()

    #print the size and is the queue is empty to check if it is empty
    print(f'queue Size = {my_q.size()}')
    print(f'If queue is empty =  {my_q.empty()}')
    print(t.center(50,'-'))
    #add a new item to the queue
    my_q.push_back("Joshua")
    my_q.push_back("Carlos")
    my_q.push_back("Chuy")
    my_q.push_back("Gustavo")
    my_q.push_back("Fabian")

    #function to don't repeat the results in the console
    #print the sieze, if the queue is empty to check the queue is empty and the first item in the queue and the last
    def print_queue(my_q):
        print(f'queue Front = {my_q.front()}')
        print(f'queue Back = {my_q.back()}')
        print(f'queue Size = {my_q.size()}')
        print(f'If queue is empty =  {my_q.empty()}')
        print(t.center(50,'-'))
    print_queue(my_q)

    for element in my_q.iter():
        print(element)

    #delete the an item in the queue
    my_q.pop_front()
    print_queue(my_q)
    #add it again in the queue
    my_q.push_back("Joshua")
    print_queue(my_q)
    #finally show the queue again
    for element in my_q.iter():
        print(element)
