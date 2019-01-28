'''
@author-name: Rishab Katta
'''
from stack import *
from queue import *
from ListQueue import *
from ListStack import *

def router_test():
    '''
    This function is written to test the implementations of Stack and Queue using Ringbuffer and Python List.
    Performs various operations like insert, push, pop, enqueue, dequeue etc. I'm using ListStack and ListQueue as ref
    to check if my implementations are correct or not.
    '''

    stack = Stack(20)
    queue = Queue(20)
    liststack = ListStack(20)
    listqueue = ListQueue(20)

    for i in range(20):
        stack.push(i)
        queue.enqueue(i)
        liststack.insert(i)
        listqueue.insert(i)
    print(stack)
    print(queue)
    print(liststack)
    print(listqueue)

    for i in range(20,31):
        stack.push(i)
        queue.enqueue(i)
        liststack.insert(i)
        listqueue.insert(i)

    print(" ")
    print(stack)
    print(queue)
    print(liststack)
    print(listqueue)

    for _ in range(10):
        stack.pop()
        queue.dequeue()
        liststack.remove()
        listqueue.remove()

    print(" ")
    print(stack)
    print(queue)
    print(liststack)
    print(listqueue)

    for _ in range(10):
        stack.pop()
        queue.dequeue()
        liststack.remove()
        listqueue.remove()

    print(" ")
    print(stack)
    print(queue)
    print(liststack)
    print(listqueue)

    for _ in range(10):
        stack.pop()
        queue.dequeue()
        liststack.remove()
        listqueue.remove()

    print(" ")
    print(stack)
    print(queue)
    print(liststack)
    print(listqueue)

    for i in range(20):
        queue.enqueue(i)
        listqueue.insert(i)

    print(" ")
    print(queue)
    print(listqueue)
    print("Queue size: " + str(queue.queue_size()))
    print(" ")

    for _ in range(20):
        stack.push(queue.peek())
        liststack.insert(queue.peek())
        queue.dequeue()
        listqueue.remove()
    print(stack)
    print(liststack)

    print("Stack size: " + str(stack.stack_size()))

    for _ in range(20):
        queue.enqueue(stack.peek())
        listqueue.insert(stack.peek())
        stack.pop()

    print(" ")
    print(queue)
    print(listqueue)
    print(queue.queue_size())


if __name__ == '__main__':
    router_test()