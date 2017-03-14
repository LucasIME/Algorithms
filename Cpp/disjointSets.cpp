#include <iostream>
#include <map>
#include <vector>

using namespace std;

template<typename T>
class disjoint_set{
public:
    T val;
    disjoint_set<T> *parent;
    int h;
    
    disjoint_set(T x){
        this->val = x;
        this->parent = NULL;
        this->h = 1;
    }
    
    
    disjoint_set<T>* findSet(){
        disjoint_set<T> *node = this;
        while(node->parent != NULL) node = node->parent;
        return node;
    }
    
    void unite(disjoint_set<T> *y){
        disjoint_set<T> *rx = this;
        disjoint_set<T> *ry = y;
        rx =  rx->findSet();
        ry = ry->findSet();
        if(rx->h < ry->h) rx->parent = ry;
        else if (rx->h > ry->h) ry->parent = rx;
        else{
            ry->parent = rx;
            rx->h++;
        }
    }
    
};

int main(){
    map<int, disjoint_set<int> * > m;
    m[3] = new disjoint_set<int>(3);
    m[7] = new disjoint_set<int>(7);
    m[4] = new disjoint_set<int>(4);
    m[5] = new disjoint_set<int>(5);
    m[6] = new disjoint_set<int>(6);
    m[20] = new disjoint_set<int>(20);
    m[2] = new disjoint_set<int>(2);
    m[9] = new disjoint_set<int>(9);
    m[16] = new disjoint_set<int>(16);
    m[4]->unite(m[9]);
    m[3]->unite(m[7]);
    m[2]->unite(m[16]);
    m[6]->unite(m[5]);
    m[5]->unite(m[20]);
    m[3]->unite(m[5]);
    for (auto x: m){
        cout << x.first <<  " " <<  x.second->findSet()->val << endl;
    }
    return 0;
}