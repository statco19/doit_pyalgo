from typing import Any, Type

class Node(object):
	"Node class for LinkedList"
	
	def __init__(self, data: Any = None, next= None):
		self.data = data
		self.next = Node

class LinkedList(object):
	"LinkedList class"
	
	def __init__(self) -> None:
		self.no = 0
		self.head = None
		self.current = None
		
	def __len__(self) -> int:
		return self.no
		
	def __search__(self, data: Any) -> int:
		"searching the Node which has data"
		
		idx = 0
		ptr = self.head
		
		while ptr is not None:
			if ptr.data == data:
				self.current = ptr
				return idx
			idx += 1
			ptr = ptr.next
			
		return -1
		
	def __contains__(self, data: Any) -> bool:
		"checking if the linked list has the data"
		
		return self.__search__(data) >= 0
		
	def add_first(self, data: Any) -> None:
		"adding a Node at the first"
		
		ptr = self.head
		self.head = self.current = Node(data, ptr)
		self.no += 1
		
	def add_last(self, data: Any) -> None:
		"adding a Node at the last"
		
		if self.head is None:
			self.add_first(data)
		
		else:
			ptr = self.head
			while ptr.next is not None:
				ptr = ptr.next
			
			ptr.next = self.current = Node(data, None)
			self.no += 1
