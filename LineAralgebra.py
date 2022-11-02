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

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("It isn't a Matrix class")

        return self.array == other.array

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("It isn't a Matrix class")

        if self.size != other.size:
            raise ValueError('The matrices must be of the same size.')

        array = self.array.copy()
        for x, y in zip(array, other.array):
            for a, b in zip(x, y):
                x[x.index(a)] = a + b

        return Matrix(array)
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("It isn't a Matrix class")

        if self.size != other.size:
            raise ValueError('The matrices must be of the same size.')

        array = self.array.copy()
        for x, y in zip(array, other.array):
            for a, b in zip(x, y):
                x[x.index(a)] = a - b

        return Matrix(array)


    @property
    def n_rows(self): #Lenght list array
        return len(self.array)

    @property
    def n_cols(self): #Lenght columns list
        if len(self.array) == 0:
            return 0
        return len(self.array[0])

    @property
    def size(self): #(Len array, len columns list)
        return (self.n_rows, self.n_cols)

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

    def add_row(self, row, index=None):#Add row to array

        if not isinstance(row, list):
            raise TypeError('To create a matrix you need to pass a nested list of values.')

        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError('The values must be of type int or float.')

        if len(row) != self.n_cols:
            raise ValueError('The row must be the same length as the number of columns in the matrix.')

        if index is None:
            self.array.append(row)
        else:
            self.array.insert(index, row)

    def add_column(self, column, index=None): #Add column to array

        if not isinstance(column, list):
            raise TypeError('To create a matrix you need to pass a nested list of values.')

        for x in column:
            if not isinstance(x, (int, float)):
                raise TypeError('The values must be of type int or float.')

        if len(column) != self.n_rows:
            raise ValueError('The row must be the same length as the number '
                'of columns in the matrix.')

        if index is None:
            for i in range(0, len(self.array)):
                self.array[i].append(column[i])

        else:
            for i in range(0, len(self.array)):
                self.array[i].insert(index, column[i])

    def transpose(self):    #Changing columns with rows
        array = [[] for x in range(self.n_cols)]
        for x in range(self.n_cols):
            for y in range(self.n_rows):
                array[x].append(self.array[y][x])
        return Matrix(array)

    def multiply_elementwise(self, other): #Multiplication elements
        if not isinstance(other, Matrix):
            raise TypeError("It isn't a Matrix class")

        if self.size != other.size:
            raise ValueError('The matrices must be of the same size.')

        array = []
        for i in range(self.n_rows):
            rows = []
            for x, y in zip(self.array[i], other.array[i]):
                rows.append(x*y)
            array.append(rows)
        return Matrix(array)

    @classmethod
    def dot(cls, row, column):
        if not isinstance(row, list) and not isinstance(column, list):
            raise TypeError("It isn't a list")
        if len(row) != len(column):
            raise ValueError('The lists must be of the same size.')
        array = 0
        for x, y in zip(row, column):
            array += x*y

        return array

