# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name: Molly-Marie Richards

#  Student UT EID: mmr2537

#  Partner Name: Juan Zambrano

#  Partner UT EID: jez346

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 4/2/18

#  Date Last Modified: 4/8/18

class Matrix(object):
	def __init__(self, row = 0, col = 0):
		self.row = row
		self.col = col
		self.matrix = []

	# perform matrix addition
	def __add__(self, other):
		if (self.col != other.col or self.row != other.row):
			return None

		mat = Matrix(self.row, self.col)
		for i in range(self.row):
			row = []
			for j in range(self.col):
				row.append(self.matrix[i][j] + other.matrix[i][j])
			mat.matrix.append(row)
		return mat

	def __mul__(self, other):
		if (self.col != other.row):
			return None

		mat = Matrix(self.row, other.col)
		for i in range(self.row):
			row = []
			for j in range(other.col):
				sum = 0
				for k in range(other.row):
					sum += self.matrix[i][k] * other.matrix[k][j]
				row.append(sum)
			mat.matrix.append(row)
		return mat

	def __str__(self):
		s = ''
		for i in range(self.row):
			for j in range(self.col):
				s = s + format(str(self.matrix[i][j]), ">5")
			s = s + "\n"
		return s

def read_matrix(in_file):
	line = in_file.readline().rstrip("\n").split()
	row = int(line[0])
	col = int(line[1])

	mat = Matrix(row, col)

	for i in range(row):
		row = in_file.readline().rstrip("\n").split()
		for j in range(col):
			row[j] = int(row[j])
		mat.matrix.append(row)
	line = in_file.readline()
	return mat

def main():

	in_file = open("matrix.txt", "r")

	print("Test Matrix Addition")
	matA = read_matrix(in_file)
	print(matA)
	matB = read_matrix(in_file)
	print(matB)

	matC = matA + matB
	print(matC)

	print("Test Matrix Multiplication")
	matP = read_matrix(in_file)
	print(matP)
	matQ = read_matrix(in_file)
	print(matQ)
	matR = matP * matQ
	print(matR)

	in_file.close()

main()