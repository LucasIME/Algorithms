__author__ = 'Lucas'

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i> -1 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

v = [5,2,4,6,1,3]

insertion_sort(v)

print(v)
