
def make_square ( n ):
    ls = []
    for i in range(n):
        ls.append([])
        for j in range(n):
            ls[i].append(0)
#A list of a nxn matrix that is populated with zeros has been Created
# Algo for filling in matrix of zero values to form a magic square
    ls[n-1][n//2] = 1
    n = n-1
    j = n//2
    for k in range(2,((n+1)**2 +1)): # fill in square from 2 to n*n
        if(i == n and j == n): # condition 1
            i -=1
            ls[i][j] = k
        elif(i == n and j != n): #condition 2
            i = 0
            j += 1
            ls[0][j] = k
        elif(i != n and j == n): #condition 3
            i += 1
            j = 0
            ls[ i][0] = k
        else: # final condition
            i += 1
            j += 1
            if(ls[i][j] == 0):
                ls[i][j] = k
            else:
                i -= 2
                j -= 1
                ls[i][j] = k
    print_square(ls) # call function to print
    check_square(ls) # call function to check
# Print the magic square in a neat format where the numbers
# are right justified
def print_square ( magic_square ):
    for row in magic_square:
        for element in row:
            print(format(element,'2d'), end = "  ")
        print()
# Check that the 2-D list generated is indeed a magic square
def check_square ( magic_square ):
#sum of rows
    row_check = []
    for i in range(len(magic_square)):
        sum_row = 0
        for j in range(len(magic_square)):
            sum_row += magic_square[i][j]
        row_check.append(sum_row)
    column_check = []
#sum of columns
    for i in range(len(magic_square)):
        sum_column = 0
        for j in range(len(magic_square)):
            sum_column += magic_square[j][i]
        column_check.append(sum_column)
# sum of diagonals left to right
    sum_diagonal_LR = 0
    for i in range(len(magic_square)):
        sum_diagonal_LR += magic_square[i][i]
#sum of diagonals right to left
    sum_diagonal_RL = 0
    for j in range(len(magic_square)):
        sum_diagonal_RL += magic_square[i][len(magic_square) - 1 - j]
#check if sum of rows and columns are equal to each other
    for i in range(len(row_check)):
        if(row_check[i] != row_check[i - 1]):
            print(" The matrix is not a magic square.")
        elif(column_check[i] != column_check[i-1]):
            print(" The matrix is not a magic square.")
        elif(column_check[i] != row_check[i]):
            print(" The matrix is not a magic square.")
#check if diagonals are equal to each other
    if(sum_diagonal_RL != sum_diagonal_LR):
        print(" The matrix is not a magic square.")
    print("")
    print("Sum of row = ",str(sum_diagonal_LR))
    print("Sum of column = ",str(sum_diagonal_LR))
    print("Sum diagonal (UL ro LR) = ",str(sum_diagonal_LR))
    print("Sum diagonal (UR ro LL) = ",str(sum_diagonal_RL))
    print("")
def main():
  # Prompt the user to enter an odd number 3 or greater
  print("")
  odd_num = int(input("Please enter an odd number: "))
  # Check the user input
  while(odd_num%2 == 0 or odd_num < 3):
      odd_num = int(input("Please enter an odd number: "))
  print("")
  print("Here is a "+ str(odd_num) +" x "+ str(odd_num)+ " magic square: ")
  print("")
  # Create the magic square
  square = make_square(odd_num)
main()
