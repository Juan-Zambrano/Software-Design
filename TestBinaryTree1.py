#  File: TestBinaryTree.py

#  Description: classes and methods for a binary tree

#  Student's Name: Alyssa Jones

#  Student's UT EID: adj484

#  Partner Name: Juan Zambrano

#  Partner UT EID: jez346

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 13 April

#  Date Last Modified: 14 April




class Node (object):
	def __init__(self, data = None):
		self. data = data
		self.lchild = None
		self.rchild = None

	# check if node is a leaf
	def is_leaf(self):
		if self.lchild != None or self.rchild != None:
			return False
		return True

	def __str__(self):
		s = str(self.data)
		return s

class Tree (object):
	def __init__(self):
		self.root = None
		self.count = 0

	# search for a node with a key
	def search (self, key):
		current = self.root
		while current != None and current.data != key:
			if key < current.data:
				current = current.lchild
			else:
				current = current.rchild
		return current

	# insert a node in a tree
	def insert( self, val):
		new_node = Node(val)

		if self.root == None:
			self.root = new_node
		else:
			current = self.root
			parent = self.root
			while current != None:
				parent = current
				if val < current.data:
					current = current.lchild
				else:
					current = current.rchild
			if val < parent.data:
				parent.lchild = new_node
			else:
				parent.rchild = new_node
		self.count += 1

	
	# returns true if two binary trees are similar
	def is_similar(self, pNode):
		if self.is_similar_helper(self.root, pNode.root):
			return True
		else:
			return False



	# helper function for is_similar
	def is_similar_helper(self, aNode, bNode):
		if aNode == None and bNode == None:
			return True
		else:
			if (aNode == None and bNone != None) or (aNode != None and bNode == None):
				return False
			elif (aNode.is_leaf() and bNode.is_leaf() == False) or (bNode.is_leaf() and aNode.is_leaf() == False):
				return False
			elif aNode.data != bNode.data:
				return False
			else:
				return self.is_similar_helper(aNode.lchild, bNode.lchild)
				return self.is_similar_helper(aNode.rchild, bNode.rchild)

	# prints out all nodes at the given level
	def print_level(self,level):
		currentl = self.root
		currentr = self.root
		values = []
		
		print("work")
		if(level != self.get_height_helper(currentl) and level != self.get_height_helper(currentr)):
			i = 1
			while( i != level + 1):
				if(i < level):
					currentl = currentl.lchild
					currentr = currentr.rchild
				else:
					values.append(currentl.data)
					values.append(currentr.data)	
				i+=1
		else:
			currentl = currentl.lchild.lchild
			currentr = currentr.rchild.rchild
			values.append(currentl.data)
			values.append(currentr.data)

		print(values)
		return


	# returns the height of the tree
	def get_height(self):

		return(self.get_height_helper(self.root))

	def get_height_helper(self, aNode):
		if aNode is None:
			return 0
		if aNode.is_leaf():
			return 1
		return (1 + max(self.get_height_helper(aNode.lchild), self.get_height_helper(aNode.rchild)))

	# returns number of nodes in the tree
	def num_nodes(self):
		if self.root == None:
			return 0
		else:
			return(1 + self.num_nodes_helper(self.root.lchild) + self.num_nodes_helper(self.root.rchild))

	def num_nodes_helper(self, aNode):

		if aNode == None:
			return 0
		return (1 + self.num_nodes_helper(aNode.lchild) + self.num_nodes_helper(aNode.rchild))


def main():
	# create three trees - two are the same, one is different
	
	tree1_data = [6, 5, 7, 2, 4, 8, 9]
	tree2_data = [6, 5, 7, 2, 4, 8, 9]
	tree3_data = [1, 2, 3, 4, 5, 6, 7]
	tree1 = Tree()
	tree2 = Tree()
	tree3 = Tree()
	for i in range(len(tree1_data)):
		tree1.insert(tree1_data[i])
		tree2.insert(tree2_data[i])
		tree3.insert(tree3_data[i])
	
	# print levels of two trees that are different
	print("print_level test")
	tree1.print_level(4)
main()