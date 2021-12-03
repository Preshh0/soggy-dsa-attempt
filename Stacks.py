# #LIFO - last in, first out
# my_stack = list()
# my_stack.append(4)
# my_stack.append(7)
# my_stack.append(12)
# my_stack.append(19)
# print(my_stack)

# print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack)

#Wrapper Class Example
class ListStack:
     def __init__(self):
             self._L = []
     def push(self, item):
             self._L.append(item)
     def pop(self):
         if len(self._L) <= 0:
             return None
         else:
             return self._L.pop()
     def peek(self):
         if len(self._L) <= 0: 
             return None
         else:
             return self._L[-1]
     def __len__(self):
             return len(self._L)
     def isempty(self):
             return len(self) == 0
     def __str__(self):
             return str(self._L)


L=ListStack()
L.push(3)
L.push(5)
print(L.peek())
print(L.isempty(), f"There are about {len(L)} inputs.")