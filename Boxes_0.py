#  File: Boxes.py

#  Description:

#  Student Name: Juan Zambrano

#  Student UT EID: jez346

#  Partner Name: Audrey Mcnay

#  Partner UT EID:alm5735

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created:

#  Date Last Modified:

def does_fit (box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

def subsets (a, b, lo, size, li):
  if lo == len(a):
    if len(b) == size:
      li.append(b)
    return li
  else:
    c = b[:]
    b.append(a[lo])
    subsets(a, b, lo + 1, size, li)
    subsets(a, c, lo + 1, size, li)

def main():
  # open file for reading
  print("dsfsf")
  in_file = open ('boxes.txt', 'r')

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create empty list of boxes
  box_list = []
  print("print something")

  # read the list of boxes from file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for i in range (len(box)):
      box[i] = int (box[i])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  # sort the box list
  box_list.sort()
  print (box_list)


  # create a list that will hold the nested boxes
  li = []
  # create a variable for the size of the nested boxes
  nested_size = 0
  # get all subsets of boxes
  b = []
  for i in range(len(box_list)):
    subsets(box_list[i], b, 0,li)
    print('something')

  # for each subset check if they all fit
  for i in range(len(li)):
    for j in range(len(i)):
      if does_fit(li[i][j], li[i][j+1]) == False:
        li.remove(li[i])
        i = i-1
        break
      else:
        continue

  # add to list
  largest_size = len(max(li,key=len))
  for i in li:
    if len(i) != largest_size:
      li.remove(i)
    else:
      continue

  print(li)
main()
