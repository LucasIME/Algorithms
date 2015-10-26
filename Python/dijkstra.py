from priorityQueue import priorityQueue

class Node():
    def __init__(self, x):
        self.val = x
        self.childs = {}

def dijkstra(noi, vertices):
    q = priorityQueue()
    dist = {}
    for v in vertices:
        dist[v] = float('inf')
        q.insert((float('inf'),v))
    dist[noi] = 0
    q.decreaseKey(0, noi)
    while q.size > 0:
        u = q.extractMin()
        for v in u.childs:
            if dist[v] > dist[u] + u.childs[v]:
                dist[v] = dist[u] + u.childs[v]
                q.decreaseKey(dist[v], v)
    return dist

def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    a.childs[b] = 3
    a.childs[c] = 4
    a.childs[d] = 7
    b.childs[e] = 5
    b.childs[f] = 10
    c.childs[g] = 13
    c.childs[i] = 2
    d.childs[h] = 3
    d.childs[b] = 11
    e.childs[d] = 14
    v = [a,b,c,d,e,f,g,h,i]
    resp  = dijkstra(a,v)
    for key in resp:
        print(key.val, resp[key] )

if __name__ == "__main__":
    main()
