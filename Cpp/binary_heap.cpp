#include <iostream>
#include <vector>

using namespace std;

class binary_heap{
public:
	vector<int> heap;
	int size;

	binary_heap(){
		this->heap.push_back(0);
		this->size = 0;
	}

	void up(int i){
		while (i > 1){
			if(this->heap[i] < this->heap[i/2]){
				int aux = this->heap[i/2];
				this->heap[i/2] = this->heap[i];
				this->heap[i] = aux;
			}
			i/=2;
		}
	}

	void down(int i){
		while (2*i <= this->size){
			int minChildIndex = this->get_min_child(i);
			if(this->heap[i] > this->heap[minChildIndex]){
				swap(this->heap[i], this->heap[minChildIndex]);
			}
			else break;
			i = minChildIndex;
		}
	}

	int get_min_child(int i){
		if(2*i +1 > this->size) return 2*i;
		else{
			if(this->heap[2*i] < this->heap[2*i+1]) return 2*i;
			else return 2*i +1;
		}
	}

	void insert(int x){
		this->heap.push_back(x);
		this->size++;
		this->up(this->size);
	}


	int extract_min(){
		int resp = this->heap[1];
		this->heap[1] = this->heap[this->size];
		this->heap.pop_back();
		this->size--;
		this->down(1);
		return resp;
	}
};

int main(){
	binary_heap h;
	int myints[] = {3,2,6,7,8,15};
	vector<int> v(myints, myints + sizeof(myints)/sizeof(int));
	for(int i=0; i < v.size(); i++){
		h.insert(v[i]);
		for(int j=0; j < h.heap.size(); j++) cout << h.heap[j] << " ";
		cout << endl;
	}
	while(h.size > 0){
		cout << h.extract_min() << endl;
	}
	return 0;
}
