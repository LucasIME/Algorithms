#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;

template<typename T>
void insertion_sort(vector<T> &A){
    for(int j=1; j < A.size(); j++ ){
        T key = A[j];
        int i = j-1;
        while ( i > -1 && A[i] > key){
            A[i+1] = A[i];
            i--;
        }
        A[i+1] = key;
    }
}

int main(){
    int myints[] = {5,2,4,6,1,3 };
    vector<int> v(myints, myints + sizeof(myints)/sizeof(int));
    insertion_sort(v);
    for(int i =0; i< v.size(); i++) cout << v[i] <<" ";
    //system("pause");
    return 0;
}
