# Project and File Information
#	File: Tree.py
#	Project: NOAGI16
#	https://github.com/darkAco/noagi16
#

# File Description:
#	Contains the class 'Tree', which itself contains the class
#	'Node'. These classes are used to create a "Parse"-Tree.
#

# Class 'Tree'
#	A Tree describes the relationship between certain values of any type.
#	It consists of nodes, which each hold a value (of any type) and can,
#	but not necessarily have to, have another Node as Parent and or Child.
#	The class is not destinated to be used in circles, e.g.:
#		NodeA is Parent of NodeB and NodeB is Parent of NodeA
class Tree():
	class Node():
		def __init__(self, Value):
			self.parent = None
			self.childs = []
			self.value = Value
	def __init__(self):
		self.root = None
