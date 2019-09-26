#include <bits/stdc++.h>
#include "sorting.hpp"
#include "seqLinearList.hpp"
using namespace std;

template<class Item>
void printList(LinearList<Item>& A, int low, int high){
    for (int i = low; i < high; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
}

int main(){
    int n,k;
    cout << "Enter n k: ";
    cin >> n >> k;
    cout << "1 for healthy 0 for unhealthy."<<endl;
    LinearList<int> A(n);
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    Sort<int> S;
    S.quickSort(A,0,n);
    cout << "Part 1: " << endl;
    for (int i = 0; i < (int)n/2; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
    cout << "Part 2" << endl;
    for (int i = (int)n/2; i < n; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
    cout << "There no need if he sorts things first.";
    
}
