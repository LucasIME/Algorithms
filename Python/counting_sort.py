def counting_sort(A):
    k = max(A)
    C = [0 for n in range(k+1)]
    B = [0 for p in A]
    for i in range(1, len(A)):
        C[A[i]] =  C[A[i]]+1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]] = A[i]
        C[A[i]] = C[A[i]] -1
    return B
def main():
    v = [6,4,7,3,7,9,9,2,15]
    v = counting_sort(v)
    print v
if __name__ == '__main__':
    main()
