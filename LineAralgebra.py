class Matrix:

    def __init__(self, array):
        if len(array) != 0:
            if not isinstance(array, list):
                raise TypeError('To create a matrix you need to pass a nested list of values.')
            for x in array:
                leng_list = len(array[0])
                if not isinstance(x, list):
                    raise TypeError('Each element of the array (nested list) must be a list.')
                elif len(x) != leng_list:
                    raise TypeError('All columns must be the same length.')
            for x in array:
                for y in x:
                    if not isinstance(y, (int, float)):
                        raise TypeError('The values must be of type int or float.')
            self.array = array
        else:
            self.array = []


    def __repr__(self):
        return str(self.array)


mat = Matrix([[1,1], [1,1]])

print(mat)