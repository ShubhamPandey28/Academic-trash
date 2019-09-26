#include <bits/stdc++.h>
#include "seqLinearList.hpp"
#include "sorting.hpp"

using namespace std;
int n,x;

template<class Item>
void printList(LinearList<Item>& A, int low, int high){
    for (int i = low; i < high; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
}

int main(){
    cin >> n;
    LinearList<int> A(n);
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        A.insert(i+1,x);
    }
    Sort<int> S;
    
    S.quickSort(A,0,n);
    printList(A,0,n);
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    S.mergeSort(A,0,n-1);
    printList(A,0,n);
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    S.heapSort(A,0,n);
    printList(A,0,n);
    
    
}