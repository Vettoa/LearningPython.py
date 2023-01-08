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
        if len(self.__data) == 0:
            raise EmptyStackError('The stack is Empty')
        else:
            return self.__data.pop(0)
