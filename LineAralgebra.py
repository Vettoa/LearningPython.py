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
    def n_rows(self): #Lenght list array
        return len(self.array)

    @property
    def n_cols(self):   #Lenght nested list
        if len(self.array) == 0:
            return 0
        else:
            return len(self.array[0])

    @property
    def size(self): #(Len array, len nested list)
        return (self.n_rows, self.n_cols)\

    @property
    def is_square_matrix(self): #Checking the matrix is a square matrix
        if self.n_cols == self.n_rows:
            return True
        else:
            return False

    def zero(self): #Changing value in array to 0
        zero = [[0 for x in range(0, self.n_cols)] for y in range(0, self.n_rows)]
        return zero

    def identity(self): #Unit matrix for square matrices
        if self.is_square_matrix:
            matrix = self.zero()
            for x in range(0, len(matrix)):
                matrix[x][x] = 1
            return matrix
        else:
            return None

matr = Matrix([[1,2,3],[1,2,3]])

print(matr.identity())
#print(matr.array)