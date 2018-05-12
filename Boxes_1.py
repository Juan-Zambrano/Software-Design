#  Description: Finds the largest sub-set of boxes and the max amount given[l,w,h]
def does_fit(box): #takes in subset list and checks if they fit into each other.
    for i in range(len(box) - 1):
        box1=box[i]
        box2=box[i+1]
        if(((box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])) == False):
            return False
    return True   
def subsets (a, b, lo, li):
    if (lo == len(a)):
        if(does_fit(b) == True):
            li.append(b)
        return
    else:
        c = b[:]
        b.append (a[lo])
        subsets (a, b, lo + 1, li)
        subsets (a, c, lo + 1, li)
def main():
    with open('boxes.txt','r') as f:
        line = f.readline().strip() #reads number listed that indicates number of lines in file
        box_list = [] #input list
        li = [] #output list 
        for i in range(int(line)):
            box = f.readline().strip().split()
            for i in range(len(box)):
                box[i] = int(box[i])
            box.sort()
            box_list.append(box)
    box_list.sort() # sort the box list
    subsets(box_list,[],0,li) #call function subsets()  
    print("Largest Subset of Nesting Boxes")
    for i in [x for x in li if (len(x) == (len(max(li,key = len))))]:
        for j in i:
            print(j)
        print() 
main()