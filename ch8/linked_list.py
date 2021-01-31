from typing import Any, Type

class Node(object):
	"Node class for LinkedList"
	
	def __init__(self, data: Any = None, next= None):
		self.data = data
		self.next = next

class LinkedList(object):
	"LinkedList class"
	
	def __init__(self) -> None:
		self.no = 0
		self.head = None
		self.current = None
		
	def __len__(self) -> int:
		return self.no
		
	def search(self, data: Any) -> int:
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
		
		return self.search(data) >= 0
		
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
			
	def remove_first(self) -> None:
		"remove the head node"
		
		if self.head is not None:
			self.head = self.current = self.head.next
			self.no -= 1
	
	def remove_last(self) -> None:
		"remove the last node"
		
		if self.head is not None:
			if self.head.next is None:
				self.remove_first()
			else:
				ptr=self.head
				pre=self.head
				
				while ptr.next is not None:
					pre = ptr
					ptr = ptr.next
				pre.next = None
				self.current = pre
				self.no -= 1
				
	def remove(self, p)	-> None: # p is Node type class
		"remove the designated node"
		
		if self.head is not None:
			if p is self.head:
				self.remove_first()
			else:
				ptr = self.head
				while ptr.next is not p:
					ptr = ptr.next
					if ptr.next is None:
						print("Can't find the node.'")
						return
				
				ptr.next = p.next
				self.current = ptr
				self.no -= 1
				
	def remove_current_node(self) -> None:
		self.remove(self.current)
		
	def clear(self) -> None:
		while self.head is not None:
			self.remove_first()
		self.current = None
		self.no = 0
			
	def next(self) -> bool:
		if self.current is None or self.current.next is None:
			return False
		else:
			self.current = self.current.next
		return True
	
	def print_current_node(self) -> None:
		"print current node's data"
		
		if self.current is None:
			print("No current node exists.")
		else:
			print(self.current.data)
			
	def print(self) -> None:
		"print every node's data"
		
		ptr = self.head
		
		while ptr is not None:
			print(ptr.data)
			ptr = ptr.next
			
	def __iter__(self):  # -> LinkedListIterator:
		"return iterator"
		
		return LinkedListIterator(self.head)
		
class LinkedListIterator (object):
	
	def __init__(self, head): # head is Node type
		self.current = head
		
	def __iter__(self): # -> LinkedListIterator:
		return self
		
	def __next__(self) -> Any:
		if self.current is None:
			raise StopIteration
		else:
			data = self.current.data
			self.current = self.current.next
			return data
