# from math import *

"""Matrix class
"""
class Matrix:
    """matrix class(row,column)
    available funtions :
    enter_matrix() - enters matrix of the size
    deleterow(row_no) - returns matrix with deleted row
    deletecolumn(column_no)- returns matrix with deleted column
    detrminant() - returns determinant of matrix as float
    min() - returns minor of the matrix
    cofactor() - returns cofactor of matrix
    adj() - returns adj
    inverse() - returns inverse of matrix
    getcolumn(column_no) - returns a coulm as a list
    transpose() - returns transpose of a matrix
    issquare() 
    isdiagonal()
    isscalar()
    isidentity()
    append(matrix1,matrix2 .....)
    Operators : + , - , *,/"""

    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.matrix = []


    def enter_matrix(self):

        for i in range(self.row):
            a = input("enter a row")
            b = a.split()
            row = []
            for j in range(self.column):
                row.append(int(b[j]))
            self.matrix.append(row)


    def deleterow(self, row):

        matrix = []
        for i in range(self.row):
            if row != i:
                matrix.append(self.matrix[i])
        mat = Matrix(self.row - 1, self.column)
        mat.matrix = matrix
        return mat


    def deletecolumn(self, column):

        matrix = []
        for i in range(self.row):
            row = []
            for j in range(self.column):
                if column != j:
                    row.append(self.matrix[i][j])
            matrix.append(row)
        mat = Matrix(self.row, self.column - 1)
        mat.matrix = matrix
        return mat


    def determinant(self):

        det = 0
        if self.issquare():
            if self.row == 1 and self.column == 1:
                return self.matrix[0][0]

            elif self.row == 2 and self.column == 2:
                return self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
            else:
                for i in range(self.row):
                    a = self.deleterow(i)
                    a = a.deletecolumn(0)
                    det += ((-1)**i)*self.matrix[i][0] * a.determinant()
                return det
        else:
            return False


    def min(self):

        matrix = []
        if self.issquare():
            for i in range(self.row):
                row = []
                for j in range(self.column):

                    a = self.deleterow(i)
                    a = a.deletecolumn(j)

                    row.append(a.determinant())
                matrix.append(row)
            mat = Matrix(self.row, self.column)
            mat.matrix = matrix
            return mat
        else:
            return False


    def cofactor(self):

        if self.issquare():
            minf = self.min()
            for i in range(minf.row):
                for j in range(minf.column):
                    minf.matrix[i][j] *= ((-1) ** (i + j))

            return minf

        else:
            return False


    def adj(self):

        if self.issquare():
            cofactor = self.cofactor()
            adj = cofactor.transpose()
            return adj
        else:
            return False


    def inverse(self):

        if self.issquare():
            adj = self.adj()
            det = self.determinant()
            inverse = adj/det
            return inverse
        else:
            return False


    def getcolumn(self, i):

        column = []
        for j in range(self.row):
            column.append(self.matrix[j][i])
        return column


    def transpose(self):

        matrix = []
        for i in range(self.column):
            matrix.append(self.getcolumn(i))
        mat = Matrix(self.row, self.column)
        mat.matrix = matrix
        return mat


    def issquare(self):

        if self.row == self.column:
            return True
        else:
            return False


    def isdiagonal(self):

        if self.issquare():
            for i in range(self.row):
                for j in range(self.column):
                    if i != j and self.matrix[i][j]:
                        return False
                else:
                    return True
        else:
            return False


    def isscalar(self):

        if self.isdiagonal():
            for i in range(self.row - 1):
                if self.matrix[i][i] != self.matrix[i + 1][i + 1]:
                    return False
            else:
                return True
        else:
            return False


    def isidentity(self):

        if self.isscalar() and self.matrix[0][0] == 1:
            return True
        else:
            return False

    def append(self,*args):
        matrix = list(self.matrix)
        for i in args:
            if isinstance(i , Matrix):
                for j in i.matrix:
                    matrix.append(j)
        mat = Matrix(len(args)+1 ,self.column)
        mat.matrix = matrix
        return mat

    def __mul__(self, other):

        matrix = []
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            mat = Matrix(self.row, self.column)
            for i in range(self.row):
                row = []
                for j in range(self.column):
                    row.append((self.matrix[i][j] * other))
                matrix.append(row)
            mat.matrix = matrix
            return mat

        elif isinstance(other, Matrix):
            if self.column == other.row:
                mat = Matrix(self.row, other.column)
                for i in range(self.row):
                    row = []
                    for j in range(other.column):
                        val = 0
                        col = other.getcolumn(j)
                        for k in range(self.column):
                            val += self.matrix[i][k] * col[k]
                        row.append(val)
                    matrix.append(row)
                mat.matrix = matrix
                return mat


    def __truediv__(self, other):

        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            divisor = 1.0 / other
            return self * divisor


    def __neg__(self):
        return self * -1


    def __add__(self, other):

        if isinstance(other, Matrix):
            if self.row == other.row and self.column == other.column:
                matrix = []
                for i in range(self.row):
                    row = []
                    for j in range(self.column):
                        row.append(self.matrix[i][j] + other.matrix[i][j])
                    matrix.append(row)
                mat = Matrix(self.row, self.column)
                mat.matrix = matrix
                return mat

            else:
                return False
        else:
            return False


    def __sub__(self, other):

        if isinstance(other, Matrix):
            return self + -other
        else:
            return False


    def __str__(self):

        for i in range(self.row):
            for j in range(self.column):
                print(round(self.matrix[i][j],5), end="\t\t")
            print()
        return "\n"


if __name__ == "__main__":

    mat1 = Matrix(1, 3)
    mat1.enter_matrix()

    mat2 = Matrix(1,3)
    mat2.enter_matrix()

    mat3 = Matrix(1,3)
    mat3.enter_matrix()

    mat4 = mat1.append(mat2,mat3)


    print(mat4.determinant())
    print()
