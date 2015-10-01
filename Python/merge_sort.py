def merge(v, p, q, r):
	l1 = [x for x in v[p:q+1]]
	l2 = [x for x in v[q+1:r+1]]
	l1.append('inf')
	l2.append('inf')
	i =  j = 0
	for k in range(p, r+1):
		if l1[i] <= l2[j]:
			v[k] = l1[i]
			i+=1
		else:
			v[k] = l2[j]
			j+=1
			
def merge_sort(v, i, j):
	if i < j:
		mid = (i+j)//2
		merge_sort(v, i, mid)
		merge_sort(v, mid+1, j)
		merge(v, i, mid, j)

def main():
	v = [ 3,5,1,8,4 ]
	merge_sort(v, 0, 4)
	print(v)

main()
