
class priorityQueue():
    def __init__(self):
        self.heap = [(float('-inf'),0)]
        self.map = {}
        self.size = 0

    def __swap__(self, i, j):
        self.map[self.heap[i][1]], self.map[self.heap[j][1]] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __up__(self, i):
        while i > 1:
            if self.heap[i][0] < self.heap[i//2][0]:
                self.__swap__(i, i//2)
            i//=2
    def __down__(self, i):
        while 2*i <= self.size:
            minSonIndex = self.__minChild__(i)
            if self.heap[i][0] > self.heap[minSonIndex][0]:
                self.__swap__(i, minSonIndex)
                i = minSonIndex
            else:
                break

    def __minChild__(self, i):
        if 2*i+1 > self.size:
            return 2*i
        else:
            if self.heap[2*i][0] < self.heap[2*i+1][0]:
                return 2*i
            else:
                return 2*i+1

    def insert(self, x):
        self.heap.append(x)
        self.size +=1
        self.map[x[1]] = self.size;
        self.__up__(self.size)

    def extractMin(self):
        resp = self.heap[1][1]
        self.__swap__(1, -1)
        del self.map[self.heap[-1][1]]
        del self.heap[-1]
        self.size-=1
        self.__down__(1)
        return resp

    def decreaseKey(self, newKey, obj):
        index = self.map[obj]
        self.heap[index] = (newKey, obj)
        self.__up__(index)


def main():
    a = priorityQueue();
    a.insert((1, 'teste'))
    a.insert((5, 123))
    a.insert((0, 'zero'))
    a.decreaseKey(-2, 'teste')
    a.decreaseKey(-200, 123)
    while a.size > 0:
        print(a.heap, a.map)
        print(a.extractMin())

if __name__ == '__main__':
    main()
