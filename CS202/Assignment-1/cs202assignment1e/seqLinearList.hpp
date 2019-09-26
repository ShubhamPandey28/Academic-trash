#ifndef SEQLINEARLIST_HPP
#define SEQLINEARLIST_HPP
#include <iostream>
#include <string.h>
using namespace std;

template<class Item>
class LinearList{
	private:
		int MaxSize;
		Item *element;    // 1D dynamic array
		int len;
		
	public:
		/* Default constructor. 
		 * Should create an empty list that not contain any elements*/
		LinearList(){
			this->element = nullptr;
			this->len = 0;
		}

		/* This constructor should create a list containing MaxSize elements. You can intialize the elements with any values.*/
		LinearList(const int& MaxListSize){
			this->element = (Item*)malloc(sizeof(Item)*(MaxListSize));
			this->MaxSize = MaxListSize;
			this->len = 0;
		}

		/* Destructor. 
		 * Must free all the memory contained by the list */
		~LinearList(){
			free(this->element);
		}

		/* Indexing operator.
     		 * It should behave the same way array indexing does. i.e,
     		 * LinearList L;
     		 * L[0] should refer to the first element;
     		 * L[1] to the second element and so on.
     		 * */
		Item& operator[](const int& i){
			return this->element[i];
		}; //return i'th element of list
		
		/* Returns true if the list is empty, false otherwise.
     		 * */
		bool isEmpty(){
			if(this->length()) return false;
			return true;
		}

		/* Returns the actual length (number of elements) in the list.
     		 * */
		int length(){
			return this->len;
		}

		/* Returns the maximum size of the list.
     		 * */
		int  maxSize(){
			return this->MaxSize;
		}

		/* Returns the k-th element of the list. 
		 * */
		Item  returnListElement(const int k){
			return this->element[k-1];
		}

		/* Set x to the k-th element and 
		 * return true if k-th element is present otherwise return false.
		 * */
		bool find(const int k, Item& x){
			if(this->len < k || this->element[k-1] != -100) return false;
			this->element[k-1] = x;
			return true;
		}

		/* Search for x and 
		 * return the position if found, else return 0.
		 * */
		int search(Item& x){
			for (int i = 0; i < this->len; i++)
			{
				if(this->element[i] ==  x) return i+1;
			}
			return 0;
		}

		/* Set x to the k-th element and delete that k-th element.
		 * */
		void  deleteElement(const int  k, Item& x){
			if(k <= this->len){
				if(this->len){
					x = this->element[k-1];
					
					for (int i = k-1; i < this->len; i++)
					{
						this->element[i] = this->element[i+1];
					}
					this->len--;
				}
				else{
					throw "No elements to delete in the Array.";
				}
				
			}
			else{
				throw "k must be less than this->len.";
			}
		}

		/* Insert x after k-th element.
		 * */
		void  insert(int  k, Item& x){

			if(this->len < this->MaxSize){
				for (int i = this->len; i >= k-1 ; i--)
				{
					this->element[i+1] = this->element[i];
				}
				this->element[k-1] = x;
				this->len++;
			}
			else{
				throw "Not enough space to insert.";
			}
		}
};


#endif