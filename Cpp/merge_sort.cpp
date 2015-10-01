#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;


template<typename T>
void merge(vector<T> &A, int p, int q, int r){
	int n1 = q-p+1;
	int n2 = r-q;
	int L[n1+1], R[n2+1];
	for (int i=0; i < n1 ; i++){
		L[i] = A[p+i];
	}
	for(int j=0; j< n2; j++){
		R[j] = A[q+j+1];
	}
	L[n1] = (1<<15) -1;
	R[n2] = (1<<15) -1;
	int i=0, j=0;
	for(int k=p; k <= r; k++){
		if(L[i] <= R[j]){
			A[k] = L[i];
			i++;
		}
		else{
			A[k] = R[j];
			j++;
		}
	}
}

// 0,5 => 0, 2, 5
template<typename T>
void merge_sort(vector<T> &A, int p, int r){
	if(p<r){
		int q = (p+r)/2;
		merge_sort(A, p, q);
		merge_sort(A,q+1, r);
		merge(A,p,q,r);
	}
}

int main(){
    int myints[] = {5,2,4,6,1,3};
    vector<int> v(myints, myints + sizeof(myints)/sizeof(int));
    merge_sort(v, 0, 5);
    for(int i =0; i< v.size(); i++) cout << v[i] <<" ";
    //system("pause");
    return 0;
}
