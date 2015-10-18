class Node():
	def __init__(self, x):
		self.val = x
		self.childs = []

def BFS(node):
	queue = [node]
	marked = {}
	while len(queue) > 0:
		no  = queue.pop()
		if no not in marked:
			marked[no] = 1
			print(no.val)
			for p in no.childs:
				queue.insert(0, p)

def main():
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)
	e = Node(5)
	f = Node(6)
	g = Node(7)
	h = Node(8)
	i = Node(9)
	a.childs.append(b)
	a.childs.append(c)
	a.childs.append(d)
	b.childs.append(e)
	b.childs.append(f)
	c.childs.append(g)
	c.childs.append(i)
	d.childs.append(h)
	d.childs.append(b)
	e.childs.append(d)
	BFS(a)

if __name__ == '__main__':
	main()