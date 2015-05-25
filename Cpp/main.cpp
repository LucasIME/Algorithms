#include <iostream>
#include <vector>
#include <stdlib.h>
#include<string>
#include<stdio.h>
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
    int n, carry=0, b, c;
    /*cin >> n;
    char n1[n], n2[n], resp[n+1];
    cin >> n1 >> n2;
    for (int i=n-1; i>= 0; i--){
        resp[i] = (char) (int)n1[i] ^(int) n2[i];
    }
    cout << resp;
    cout << n1 <<"x" << n2;*/
    scanf("%i", &b);
    c= b <<2 ;
    cout << b << " " << c;
    return 0;
}
