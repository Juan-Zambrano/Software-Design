'''
  File: TestLinkedList.py

  Description:

  Student's Name: Juan Zambrano

  Student's UT EID: jez346
 
  Partner's Name:

  Partner's UT EID:

  Course Name: CS 313E 

  Unique Number: 51335

  Date Created: March 29 2018

  Date Last Modified: March 30 2018
'''

class Link (object): #node
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    def __init__ (self):
        self.first = None
        #first is the root node
    # add an item at the beginning of the list
    def insert_first (self, item): 
        new_link = Link(item) #new node
        new_link.next = self.first 
        self.first = new_link
    # add an item to the end of the list
    def insert_last (self, item):
        new_link = Link(item) 
        current = self.first 
        if (current == None):
            self.first = new_link
            return
        while (current.next != None):
            current = current.next
        current.next = new_link
    # delete a link containing the item
    def delete_link (self, item):
        previous = self.first
        current = self.first
        if (current == None):
            return None
        while (current.data != item):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next      
        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next
        return current
    
    def get_num_links(self): #number of nodes
        current = self.first
        count = 0
        if(current == None):
            return 0
        
        
        elif(current.next == None):
            return 1
        else:
            while(current.next !=None):
                
                current = current.next
                count+=1
        return count
    
    # add an item in an ordered list in ascending order
    def insert_in_order (self, item):
        current = self.first
        if(current == None):
            self.insert_first(item)
            return
        elif((current.data > item)):
            self.insert_first(item)
        else:
            new_node = Link(item)
            previous = self.first
            while(current.data < item):
                if(current.next == None):
                    self.insert_last(item)
                    return
                else:
                    previous = current
                    current = current.next
            previous.next = new_node
            new_node.next = current
     
    # search in an unordered list, return None if not found
    def find_unordered (self, item):
        current = self.first
        if(current.data == None):
            return None
        else:
            while(current.data != item):
                if(current.next == None):
                    return None
                    break
                else:
                    current = current.next
            return current 
                

    # Search in an ordered list, return None if not found
    def find_ordered (self, item):
        current = self.first
        if(current.data == None):
            return None
        else:
            while(current.data != item):
                if(current.next == None):
                    return None
                    break
                elif(current.next.data > item):
                    return None
                    break
                current = current.next
            return current
        
    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        if self.first == None:
            return("None")
        string = ''
        count = 0
        current = self.first
        while(current.next != None):
            string +=str(current.data) + '  '
            current = current.next
            count+=1
            if((count)%10 == 0):
                string+='\n'
        return string

    # Copy the contents of a list and return new list
    def copy_list (self): 
        new_ls = LinkedList()
        current = self.first
        while(current != None):
            new_ls.insert_last(current.data)
            current = current.next
        return new_ls

    # Reverse the contents of a list and return new list
    def reverse_list (self):
        new_ls = LinkedList()
        current = self.first
        while(current != None):
            new_ls.insert_first(current.data)
            current = current.next
        return new_ls

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self):
        new_ls = LinkedList()
        current = self.first
        while(current != None):
            new_ls.insert_in_order(current.data)
            current = current.next
        return new_ls
            
                
    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        if(self.is_empty()):
            return True
        else:
            current = self.first
            while(current.next != None):
                if(current.data > current.next.data):
                    return False
                current = current.next
            return True
        

    # Return True if a list is empty or False otherwise
    def is_empty (self):
        if (self.first == None):
            return True
        else:
            return False

    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other):
        new_ls = LinkedList()
        current = self.first
        while(current != None):
            new_ls.insert_last(current.data)
            current = current.next
        current_other = other.first
        while(current_other != None):
            new_ls.insert_last(current_other.data)
            current_other = current_other.next
        new_ls = new_ls.sort_list()
        return new_ls
        
        
    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        if(self.get_num_links() != other.get_num_links()):
            return False
        current = self.first
        current_other = other.first
        while(current != None):
            if(current.data != current_other.data):
                return False
            current = current.next
            current_other = current_other.next
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        current = self.first
        new_ls = []
        set_ls = LinkedList()
        while(current != None):
            if(current.data in new_ls):
                pass
            else:
                set_ls.insert_last(current.data)
                new_ls.append(current.data)
            current = current.next
        return set_ls
            
def main():
    '''# Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    print("Testing insert_first() and __str__()")
    print()
    test1 = LinkedList()
    for i in range(11):
        test1.insert_first(i)
    print(test1)
    print()
    # Test method insert_last()
    print("Testing insert_last()")
    test1 = test1.insert_last(13)
    print(test1)
    print()
    # Test method insert_in_order()
    print("Testing insert_in_order()")
    fun = LinkedList()
    for i in range(30,20,-1):
        fun.insert_in_order(i)
    print(fun)
    print()
    # Test method get_num_links()
    print("Testing get_num_links()")
    print(fun.get_num_links())
    print()
    # Test method find_unordered() 
    # Consider two cases - item is there, item is not there 
    test2 = LinkedList()
    test2
    print("Testing find_unordered()")
    print("item is there")
    print(test1.find_unordered(2))
    print("item is not there")
    print(test1.find_unordered(99))
    print()
    # Test method find_ordered() 
    # Consider two cases - item is there, item is not there
    print("Testing find_ordered()")
    print("item is there")
    print(fun.find_ordered(4))
    print("item is not there")
    print(fun.find_ordered(88))
    print()
    # Test method delete_link()
    # Consider two cases - item is there, item is not there
    print("Testing method delete_link()")
    print("item is there")
    print(test1.delete_link(2))
    print("item is not there")
    print(test1.delete_link(77))
    print()
    # Test method copy_list()
    print("Testing copy_list()")
    print(test1.copy_list())
    print()
    # Test method reverse_list()
    print("Testing reverse_list()")
    print("Original list")
    print(test1)
    print('reverse list')
    print(test1.reverse_list())
    print()
    # Test method sort_list()
    print("Testing sort_list()")
    print()
    print("print unsorted list")
    unsorted_ls = LinkedList()
    for i in range(5):
        unsorted_ls.insert_last(i)
    unsorted_ls.insert_first(9)
    unsorted_ls.insert_first(7)
    print(unsorted_ls)
    print("Sorted list")
    sort_ls = unsorted_ls.sort_list()
    print(sort_ls)
    print()
    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("Testing is_sorted()")
    print("list is sorted")
    print(sort_ls.is_sorted())
    print("list is not sorted")
    print(unsorted_ls.is_sorted())
    print()
    # Test method is_empty()
    print("Testing is_empty()")
    print(sort_ls)
    print()
    print(sort_ls.is_empty())
    print()
    # Test method merge_list()
    print("Testing merge_list()")
    print('list 1')
    print(test1)
    print('list 2')
    print(sort_ls)
    print('merge of 2 list')
    print(test1.merge_list(sort_ls))
    print()
    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print('Testing is_equal()')
    ls1 = LinkedList()
    ls2 = LinkedList()
    for i in range(10):
        ls1.insert_last(i)
        ls2.insert_last(i)
    ls3 = LinkedList()
    for i in range(11,20,1):
        ls3.insert_last(i)
    print("ls1: ", ls1)
    print("ls2: ", ls2)
    print("ls3: ", ls3)
    print("ls1 == ls2 test")
    print(ls1.is_equal(ls2))
    print("ls1 != ls3 test")
    print(ls1.is_equal(ls3))
    print()
    # Test remove_duplicates()
    print('Testing remove_duplicates()')
    ls1.insert_last(5)
    ls1.insert_last(5)
    ls1.insert_last(5)
    print("ls1: ", ls1)
    print("list without duplicates")
    print(ls1.removed_duplicates())
    print()'''

if __name__ == "__main__":
    main()