#include <iostream>
#include <map>
#include <vector>

using namespace std;

template<typename T>
class Node{
public:
  T val;
  T parent;
  int h;

  Node(T x){
      this->val = x;
      this->parent = NULL;
      this->h = 1;
  }
};

template<typename T>
class disjointSet{
public:
  map<T, Node<T>* > dic;
  disjointSet(){
  }

  void makeSet(T x){
    this->dic[x] = new Node<T>(x);
  }

  T findSet(T x){
    Node<T> *node = this->dic[x];
    while(node->parent != NULL) node = this->dic[node->parent];
    return node->val;
  }

  void unite(T x, T y){
    Node<T> *rx = this->dic[this->findSet(x)];
    Node<T> *ry = this->dic[this->findSet(y)];
    if(rx->h < ry->h) rx->parent = ry->val;
    else if (rx->h > ry->h) ry->parent = rx->val;
    else{
      ry->parent = rx->val;
      rx->h++;
    }
  }

};

int main(){
  disjointSet<int> s;
  s.makeSet(3);
  s.makeSet(7);
  s.makeSet(4);
  s.makeSet(5);
  s.makeSet(6);
  s.makeSet(20);
  s.makeSet(2);
  s.makeSet(9);
  s.makeSet(16);
  s.unite(4,9);
  s.unite(3,7);
  s.unite(2,16);
  s.unite(6,5);
  s.unite(5,20);
  s.unite(3,5);
  for (map<int, Node<int>* >::iterator it = s.dic.begin(); it != s.dic.end(); it++){
    cout << it->first <<  " " <<  it->second->parent << endl;
  }
  return 0;
}
