
class binary_heap:

	def __init__(self):
		self.heap = [0]
		self.size = 0

	def up(self, i):
		while i > 1:
			if self.heap[i] < self.heap[i//2]:
				self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
			i //=2

	def down(self, i):
		while 2*i <= self.size:
			minSonIndex = self.__minChild__(i)
			if self.heap[i] > self.heap[minSonIndex]:
				self.heap[i], self.heap[minSonIndex] = self.heap[minSonIndex] , self.heap[i]
				i = minSonIndex
			else:
				break

	def __minChild__(self,i):
		if 2*i + 1 > self.size :
			return 2*i
		else:
			if self.heap[2*i] < self.heap[2*i + 1]:
				return 2*i
			else:
				return 2*i + 1

	def insert(self,x):
		self.heap.append(x)
		self.size +=1
		self.up(self.size)

	def extractMin(self):
		resp = self.heap[1]
		self.heap[1] = self.heap[-1]
		del self.heap[-1]
		self.size -=1
		self.down(1)
		return resp

def main():
	h = binary_heap()
	l = [3,2,6,7,8,15]
	for p in l:
		h.insert(p)
		print(h.heap)
	while h.size > 0:
		print(h.extractMin())

if __name__ == '__main__':
	main()
