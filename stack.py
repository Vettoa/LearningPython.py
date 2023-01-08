class EmptyStackError(Exception):
    'The stack is Empty'
    pass

class Stack:

    def __init__(self):
        self.__data = [] # stack list

    def __len__(self):
        return len(self.__data) #Checking len stack list

    def push(self, item):
        return self.__data.insert(0, item) #Adding item to the stack list on the first postiion

    def pop(self): #Showing first item from stack
        if not self.is_empty():
            raise EmptyStackError('The stack is Empty')
        else:
            return self.__data.pop(0)

    def is_empty(self): #Checking if the list is empty
        return self.__len__() > 0

techs = Stack()
techs.push('python')
techs.push('python1')
techs.push('python2')
techs.pop()
techs.pop()
techs.pop()

print(techs.is_empty())