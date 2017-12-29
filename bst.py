class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def insert_element(data,node):

	if(node.data):
		
		if(data>=node.data):
			if(node.right == None):
				node.right=Node(data)
			else:
				insert_element(data,node.right)
		if(data<node.data):
			if(node.left == None):
				node.left=Node(data)
			else:
				insert_element(data,node.left)
	else:
		node.data=data
l=[]
def inorder(node):
	global l
	if(node.left):
		inorder(node.left)
	l.append( node.data)

	if(node.right):
		inorder(node.right)
	return l


def contains(k,node):

	if(node == None):
		print False
	else:
		if(node.data==k):
			print True
		if(node.data<k):
			contains(k,node.right)
		if(node.data>k):
			contains(k,node.left)


def smallest(node):
	if(node==None):
		print "No elements present in Tree"
	if(node.left):
		smallest(node.left)
	else:
		print node.data

def largest(node):
	if(node==None):
		print "No elements present in Tree"
	if(node.right):
		largest(node.right)
	else:
		print node.data


def size(node):
	
	print(len(inorder(node)))
	

sum=0
def greaterSumTree(node):
	global sum
	if(node):
		greaterSumTree(node.right)
		temp= node.data
		node.data=sum
		sum+=temp
		greaterSumTree(node.left)

	else:
		return

array = [5, 3, 9, 7, 1, 4, 0, 12, 11, 13, 15, 6, 2, 8, 10, 14]
node=Node(array[0])

for i in array[1:]:
	insert_element(i,node)

print "contains(5): " 
contains(5,node)
print "contains(21): "
contains(21,node)
print "Print tree: ", inorder(node)
l=[]
print "size of tree: "
size(node)
print "Smallest node in tree: "
smallest(node)
print "Largest node in tree: "
largest(node)
l=[]
print "Inorder before calling greaterSumTree(): ", inorder(node)
greaterSumTree(node)
l=[]
l=inorder(node)
print "Inorder after calling greaterSumTree(): ", l