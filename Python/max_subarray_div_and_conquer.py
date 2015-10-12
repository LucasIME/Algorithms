MIN =  -100000
def find_max_crossing_subarray(A, low, mid, high):
    soma = 0
    l_sum = MIN
    for i in range(mid, low-1, -1):
        soma += A[i]
        if soma > l_sum:
            l_sum = soma
            max_left = i
    r_sum = MIN
    soma = 0
    for j in range(mid+1, high+1):
        soma += A[j]
        if soma >= r_sum:
            r_sum = soma
            max_right = j
    return (max_left, max_right, l_sum + r_sum)



def find_max_subarray(A, low, high):
    if low == high:
        return (low, high, A[low])
    else:
        mid = (low+high)//2
        l_low, l_high, l_sum = find_max_subarray(A, low, mid)
        r_low, r_high, r_sum = find_max_subarray(A, mid+1, high)
        c_low, c_high, c_sum = find_max_crossing_subarray(A, low, mid, high)
        if l_sum >= r_sum and l_sum >= c_sum:
            return (l_low, l_high, l_sum)
        elif r_sum >= l_sum and r_sum >= c_sum:
            return (r_low, r_high, r_sum)
        else:
            return (c_low, c_high, c_sum)


def main():
    v = [-2, -3,4,1,-6,55, -7, 9]
    resp = find_max_subarray(v, 0, len(v)-1)
    print(resp)


if __name__ == '__main__':
    main()
