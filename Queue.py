#FIFO - First in, first out
from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft()) #popleft means pop from the beginning of the list

#Example for Wrapper Class
class Queue:
    def __init__(self):
        self.my_queue = []
    def enqueue(self, item):
        return self.my_queue.append(item)
    def dequeue(self):
        return self.my_queue.pop()
    def get_size(self):
        return len(self.my_queue)
    def __str__(self):
        return str(self.my_queue)

my = Queue()
my.enqueue(7)
my.enqueue(8)
my.enqueue(1)
my.dequeue()
print(f"There are {my.get_size()} values in the list")
print(my)