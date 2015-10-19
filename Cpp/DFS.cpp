#include <iostream>
#include <vector>
#include <stack>
#include <set>

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


void DFS(Node<int> *node){
	stack<Node<int>*> s;
	s.push(node);
	set<Node<int>*> marked;
	while(s.empty() == false){
		Node<int> *no = s.top();
		s.pop();
		if (marked.find(no) == marked.end()){
			marked.insert(no);
			cout << no->val << " ";
			for(int i=0; i < no->childs.size(); i++){
				s.push(no->childs[i]);
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
	DFS(&a);
	return 0;
}
