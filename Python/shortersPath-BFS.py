class Node():
    def __init__(self, x):
        self.val = x
        self.childs = []

def shortestPath(node, v):
    distv = {}
    for no in v:
        distv[no] = float('inf')
    distv[node] = 0
    queue = [node]
    marked = {}
    while len(queue) > 0:
        no = queue.pop()
        if no not in marked:
            marked[no] = True
            for neigh in no.childs:
                queue.insert(0, neigh)
                if distv[neigh] == float('inf'):
                    distv[neigh] = distv[no] +1
    return distv


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
    v = [a,b,c,d,e,f,g,h,i]
    resp  = shortestPath(a,v)
    for key in resp:
        print(key.val, resp[key] )

if __name__ == '__main__':
    main()
