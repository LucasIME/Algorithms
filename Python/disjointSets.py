class Node():
    def __init__(self, x):
        self.val = x
        self.parent = None
        self.h = 1

class disjointSet():
    def __init__(self):
        self.dic = {}

    def makeSet(self, x):
        self.dic[x] = Node(x)

    def findSet(self, x):
        node = self.dic[x]
        while node.parent != None:
            node = self.dic[node.parent]
        return node.val

    def union(self,x,y):
        rx = self.dic[self.findSet(x)]
        ry = self.dic[self.findSet(y)]
        if rx.h < ry.h:
            rx.parent = ry.val
        elif rx.h > ry.h:
            ry.parent = rx.val
        else:
            ry.parent = rx.val
            rx.h +=1


def main():
    s = disjointSet()
    s.makeSet(3)
    s.makeSet(7)
    s.makeSet(4)
    s.makeSet(5)
    s.makeSet(6)
    s.makeSet(20)
    s.makeSet(2)
    s.makeSet(9)
    s.makeSet(16)
    s.union(4,9)
    s.union(3,7)
    s.union(2,16)
    s.union(6,5)
    s.union(5,20)
    s.union(3,5)
    for key in s.dic:
        print(key, s.dic[key].parent)


if __name__ == '__main__':
    main()
