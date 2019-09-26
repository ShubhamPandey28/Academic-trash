#ifndef SORTING_HPP
#define SORTING_HPP
#include <iostream>
#include "seqLinearList.hpp"

using namespace std;

template<class Item>
class Sort{
	private:
		void copyArray(Item* Arr1,int low1,int high1, Item* Arr2, int low2, int high2){
			int j = low2;
			if(high2-low2 == high1-low1){
				for (int i = low1; i < high1; i++)
				{
					Arr2[j] = Arr1[i];
					j++;
				}
			}
			else{
				throw "Length Error.";
			}
		}

		void merge(LinearList<Item>& A, int low, int mid, int high){
			int h,i,j,k;
			h=low;
			Item b[high-low+1];
			i=0;
			j=mid+1;
			while(h<=mid && j<=high)
			{
				if(A[h]<=A[j])
				b[i]=A[h++];
				else
				b[i]=A[j++];
				i++;
			}

			if( h > mid)
				for(k=j;k<=high;k++)
				b[i++]=A[k];
			else
				for(k=h;k<=mid;k++)
				b[i++]=A[k];

			for(k=0;k<=high-low;k++)
			{
				A[k+low] = b[k];
			}
		
		}

		void heapify(LinearList<Item>& A, int i,int high){
			int left =  2*i + 1;
			int right = 2*i + 2; 
			int largest = i;
			if(left < high && A[largest] < A[left]){
				largest = left;
			}
			if(right < high && A[largest] < A[right]){
				largest = right;
			}
			if(largest != i){
				swap(A[largest],A[i]);
				heapify(A,largest,high-1);
			}
		}
		
		void buildMaxHeap(LinearList<Item>& A){
			for (int i = A.length()/2; i >= 0; i--)
			{
				heapify(A,i,A.length());
			}
		}

		int partition(LinearList<Item>& A, int low, int high){
			Item pivot = A[low];
			int i = low+1;
			int j = high-1;
			while (true)
			{
				while (A[i]<=pivot && i < high)
				{
					i++;
				}
				while(A[j]>pivot && j>low){
					j--;
				}
				if(i<j){
					swap(A[i],A[j]);
				}
				else{
					break;
				}
			}
			return i-1;
		}

	public:
		Sort(){}
		~Sort(){}
		void insertionSort(LinearList<Item>& A, int low, int high){
			for (int i = low; i < high; i++)
			{
				Item tmp = A[i];
				int j = i;

				while(j > low && tmp < A[j-1]){
					A[j] = A[j-1];
					j--;
				}
				A[j] = tmp;
			}
			
		}
		void bubbleSort(LinearList<Item>& A, int low, int high){
			
			for (int i = low; i < high-1; i++)
			{
				for (int j = low; j < high-i-1; j++)
				{
					if(A[i]>A[i+1]) swap(A[i],A[i+1]);
				}
				
			}
			
		}
	 	void rankSort(LinearList<Item>& A, int low, int high){
			int rank;
			Item cpyA[high-low];
			memset(cpyA,NULL,sizeof(rank));
			for (size_t i = low; i < high; i++)
			{
				rank = 0;
				for (int j = low; j < high; j++)
				{
					if(A[i]>A[j]) rank++;
				}
				cpyA[rank] = A[i];
			}
			for (int i = low+1; i < high; i++)
			{
				if(cpyA[i] == NULL){
					cpyA[i] = cpyA[i-1];
				}
			}
			copyArray(cpyA,0,high-low,A,low,high);
			free(cpyA);
			
		}
		void selectionSort(LinearList<Item>& A, int low, int high){
			for (int i = low; i < high; i++)
			{
				int mnInd = i;
				for (int j = i; j < high; j++)
				{
					if(A[j] < A[mnInd]) mnInd = j;
				}
				swap(A[mnInd],A[i]);
			}
			
		}

		void mergeSort(LinearList<Item>& A, int low, int high){
			int mid = (low+high)/2;
			if(low < high){
				mergeSort(A,low,mid);
				mergeSort(A,mid+1,high);
				merge(A,low,mid,high);
			}
		}
		void quickSort(LinearList<Item>& A, int low, int high){
			if(low < high){
				int mid = partition(A,low,high);
				swap(A[low],A[mid]);
				quickSort(A,low,mid);
				quickSort(A,mid+1,high);
			}
		}

		void heapSort(LinearList<Item>& A, int low, int high){
			buildMaxHeap(A);
			int heaplen = A.length();
			while(heaplen > 1){
				swap(A[heaplen-1],A[0]);
				heaplen--;
				heapify(A,0,heaplen);
			}
		}
};

#endif