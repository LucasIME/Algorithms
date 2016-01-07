class Edge():
    def __init__(self, v1,v2, l):
        self.v1 = v1
        self.v2 = v2
        self.l = l

def bellmanFord(s, vSet, eSet):
    dist = {}
    for v in vSet:
        dist[v] = float('inf')
    dist[s] = 0
    for i in range(len(vSet)):
        for e in eSet:
            if dist[e.v2] > dist[e.v1] + e.l:
                dist[e.v2] = dist[e.v1] + e.l
    for e in eSet:
        if dist[e.v2] > dist[e.v1] + e.l:
            print 'Negative weight cycle found'
    return dist

def main():
    vSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    e1 = Edge('a', 'b', 3)
    e2 = Edge('a', 'c', 4)
    e3 = Edge('a', 'd', -7)
    e4 = Edge('b', 'e', -5)
    e5 = Edge('b', 'f', 10)
    e6 = Edge('c', 'g', 13)
    e7 = Edge('c', 'i', 2)
    e8 = Edge('d', 'h', 3)
    e9 = Edge('d', 'b', 11)
    e10 = Edge('e', 'd', -14)
    eSet = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
    resp = bellmanFord('a', vSet, eSet)
    for v in resp:
        print v, resp[v]

if __name__ == '__main__':
    main()