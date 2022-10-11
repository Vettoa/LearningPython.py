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
                    if not isinstance(y, (int, float)) or type(y) == bool:
                        raise TypeError('The values must be of type int or float.')
            self.array = array
        else:
            self.array = []


    def __repr__(self):
        return str(self.array)

    @property
    def n_rows(self):
        return len(self.array)

    @property
    def n_cols(self):
        if len(self.array) == 0:
            return 0
        else:
            return len(self.array[0])

    @property
    def size(self):
            return (self.n_rows, self.n_cols)\

    @property
    def is_square_matrix(self):
        if self.n_cols == self.n_rows:
            return True
        else:
            return False

mat = Matrix([[1,1],[1,1]])

print(mat.is_square_matrix)

#print(type(True))