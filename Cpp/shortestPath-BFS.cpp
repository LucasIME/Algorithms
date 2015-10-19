#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <limits>

using namespace std;

template<typename T>
class Node{
public:
	T val;
	vector<Node<T>*> childs;
	Node(T x){
		this->val = x;
	}
};

map<Node<int>*, int> shortestPath(Node<int> *node, vector<Node<int>*> v){
  map<Node<int>* , int> distv;
  queue<Node<int>*> q;
  set<Node<int>*> marked;
  for (int i=0; i < v.size(); i++) distv[v[i]] = numeric_limits<int>::max();
  distv[node] = 0;
  q.push(node);
  while(q.empty() == false){
    Node<int> *no = q.front();
    q.pop();
    if (marked.find(no) == marked.end()){
      marked.insert(no);
      for(int i =0; i < no->childs.size(); i++){
        q.push(no->childs[i]);
        if (distv[no->childs[i]] == numeric_limits<int>::max()) distv[no->childs[i]] = distv[no] + 1;
      }
    }
  }
  return distv;
}

void BFS(Node<int> *node){
	queue<Node<int>*> q;
	q.push(node);
	set<Node<int>*> marked;
	while(q.empty() == false){
		Node<int> *no = q.front();
		q.pop();
		if (marked.find(no) == marked.end()){
			marked.insert(no);
			cout << no->val << " ";
			for(int i=0; i < no->childs.size(); i++){
				q.push(no->childs[i]);
			}
		}

	}
}

int main(){
	Node<int> a(1);
	Node<int> b(2);
	Node<int> c(3);
	Node<int> d(4);
	Node<int> e(5);
	Node<int> f(6);
	Node<int> g(7);
	Node<int> h(8);
	Node<int> i(9);
	a.childs.push_back(&b);
	a.childs.push_back(&c);
	a.childs.push_back(&d);
	b.childs.push_back(&e);
	b.childs.push_back(&f);
	c.childs.push_back(&g);
	c.childs.push_back(&i);
	d.childs.push_back(&h);
	d.childs.push_back(&b);
	e.childs.push_back(&d);
  vector<Node<int>*> v;
  v.push_back(&a);
  v.push_back(&b);
  v.push_back(&c);
  v.push_back(&d);
  v.push_back(&e);
  v.push_back(&f);
  v.push_back(&g);
  v.push_back(&h);
  v.push_back(&i);
	map<Node<int>*, int> resp = shortestPath(&a, v);
  for(map<Node<int>*,int>::iterator it = resp.begin(); it != resp.end(); it++){
    cout << it->first->val << " " << it->second << endl;
  }
	return 0;
}
