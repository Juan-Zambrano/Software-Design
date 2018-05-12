 # File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name: 

#  Student UT EID:

#  Partner Name: Juan Zambrano

#  Partner UT EID: jez346

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

class Link(object):
    def __init__(self, col = 0, data = 0, next = None):
        self.col = col
        self.data = data
        self.next = next

    def __str__(self):
        s = '(' + str(self.col) + ', ' + str(self.data) + ')'
        return s

class LinkedList(object):
    def __init__(self):
        self.first = None

    def insert_last(self, col, data):
        new_link = Link(col, data)

        current = self.first
        if (current == None):
            self.first = new_link
            return

        while current.next != None:
            current = current.next

        current.next = new_link


    def insert_link(self, col, data):
        new_link = Link(col, data)

        previous = self.first
        current = self.first

        if current == None:
            self.first = new_link
            return None
        while current != None:
            if current.col < col:
                previous = current
                current = current.next
            else:
                break

        previous.next = new_link
        new_link.next = current

    def delete_link(self, col, data):
        previous = self.first
        current = self.first

        if current == None:
            return None
        while current.col != col:
            if current.next == None:
                return None
            previous = current
            current = current.next
        previous.next = current.next

        return current

    def __str__(self):
        linky_list = ''

        current = self.first

        while (current != None):
            linky_list = linky_list + str(current) + ' '
            current = current.next

        return linky_list
    
    

class Matrix(object):
    def __init__(self, row = 0, col = 0):
        self.row = row
        self.col = col
        self.matrix = []

    # perform assignment operations; matrix[row][col] = data
    def set_element(self, row, col, data):
        if data == 0:
            self.matrix[row].delete_link(col, data)
        else:
            self.matrix[row].delete_link(col, data)
            self.matrix[row].insert_link(col, data)

    def __add__(self, other):
        if (self.col != other.col or self.row != other.row):
            return None

        mat = Matrix(self.row, self.col)
        for i in range(self.row):
            row = LinkedList()
            for j in range(self.col):
                val = self.get_row(i)[j] + other.get_row(i)[j]
                if val != 0:
                    row.insert_last(j, val)
            mat.matrix.append(row)

        return mat

    def __mul__(self, other):
        if (self.col != other.row):
            return None

        mat = Matrix(self.row, other.col)
        for i in range(self.row):
            row = LinkedList()
            for j in range(other.col):
                val = 0
                for k in range(other.row):
                    val += self.get_row(i)[k] * other.get_col(j)[k]
                if val != 0:
                    row.insert_last(j, val)
            mat.matrix.append(row)
        return mat
      
    

    # return a list representing a row with the zero elements inserted
    def get_row(self,n):
        row_ls = []
        current = self.matrix[n].first    
        if(current == None):
            return row_ls
        else:
            for i in range(self.col):
                if(current.col == i and current.next != None):
                    row_ls.append(current.data)
                    current = current.next      
                elif((current.col == i) and (current.next == None)):
                    row_ls.append(current.data)      
                else:
                    row_ls.append(0)                             
        return row_ls

    # return a list representing a column with the zero elements inserted
    def get_col(self,n):
        col_ls = []
        current = self.matrix     
        if(current == None):
            return col_ls
        else:
            for i in range(self.row):
                rows = self.get_row(i)
                col_ls.append(rows[n])
            return col_ls
            

    def __str__(self):
        st = ""
        current = self.matrix
        if(current == None):
            return st
        for i in range(len(current)):
            point = self.matrix[i].first
            for j in range(self.col):
                if((point != None) and (point.col == j)):
                    st = st + str(point.data) + " "
                    point = point.next
                else:
                    st = st + str(0) + " "
            st+="\n"
                         
        return st
       
        

def read_matrix(in_file):
    line = in_file.readline().rstrip("\n").split()
    row = int(line[0])
    col = int(line[1])
    mat = Matrix(row, col)

    for i in range(row):
        line = in_file.readline().rstrip("\n").split()
        new_row = LinkedList()
        for j in range(col):
            elt = int(line[j])
            if elt != 0 :
                new_row.insert_last(j, elt)
        mat.matrix.append(new_row)
    line = in_file.readline()
    return mat

def main():
    in_file = open ("./matrix.txt", "r")

    print ("Test Matrix Addition")
    matA = read_matrix (in_file)
    print (matA)
    matB = read_matrix (in_file)
    print (matB)

    matC = matA + matB
    print (matC)

    print ("\nTest Matrix Multiplication")
    matP = read_matrix (in_file)
    print (matP)
    matQ = read_matrix (in_file)
    print (matQ)

    matR = matP * matQ
    print (matR)

    print ("\nTest Setting a Zero Element to a Non-Zero Value")
    matA.set_element (1, 1, 5)
    print (matA)

    print ("\nTest Setting a Non-Zero Elements to a Zero Value")
    matB.set_element (1, 1, 0)
    print (matB)

    print ("\nTest Getting a Row")
    row = matP.get_row(1)
    print (row)

    print ("\nTest Getting a Column")
    col = matQ.get_col(0)
    print (col)
  
    in_file.close()

main()
