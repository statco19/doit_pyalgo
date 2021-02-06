class Node (object):
	
	def __init__(self, data, prev, next): # prev, next are Node class
		self.data = data
		self.prev = prev or self
		self.next = next or self
		
class DoubleLinkedList (object):
	
	def __init__(self):
		self.head = self.current = Node()
		self.no = 0
		
	def __len__(self):
		return self.no
		
	def is_empty(self):
		return if self.head.next is self.head
		# since even an empty list has one dummy node(which has itself for its head and prev pointers),
		# we cannot judge if the list is empty by whether the number of the list is 0 or not.
		
	def search(self,data):
		cnt = 0
		ptr = self.head.next
		while ptr is not self.head:
			if ptr.data == data:
				self.current = ptr
				return cnt
			ptr = ptr.next
			cnt += 1
			
		return -1
		
	def __contains__(self, data):
		return self.search(data) >= 0
		
	def print_current_node(self):
		if self.is_empty():
			print("No current node.")
		else:
			print(self.current.data)
			
	def print(self):
		ptr = self.head.next
		
		while ptr is not self.head:
			print(ptr.data)
			ptr = ptr.next
		
	def print_reverse(self):
		ptr = self.head.prev
		
		while ptr is not self.head:
			pritn(ptr.data)
			ptr = ptr.prev
			
	def next(self):
		if self.is_empty() or self.current.next is self.head:
			return False
		self.current = self.current.next
		return True
		
	def prev(self):
		if self.is_empty() or self.current.prev is self.head:
			return False
		self.current = self.current.prev
		return True
		
	def add(self, data):
		"add a node right after the current node."
		
		node = Node(data, self.current, self.current.next)
		self.current.next = node
		self.current.next.prev = node
		self.current = node
		self.no += 1
		
	def add_first(self, data):
		"add a node at the first place."
		
		self.current = self.head
		add(data)
	
	def add_last(self, data):
		"add a node at the last place."
		
		self.current = self.head.prev
		add(data)
		
