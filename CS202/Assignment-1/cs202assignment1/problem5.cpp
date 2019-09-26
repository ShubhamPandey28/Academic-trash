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
    
    int p = n;
    LinearList<int> A(n);
    int h=1;
    for (int i = 0; i < n; i++)
    {
        A.insert(i+1,*&h);
        h++;
    }
    
    int t;
    
    int r=k;
    while(A.length() > 1){
        //printList(A,0,A.length());
        
        if(r > A.length()){
            r = r%A.length();
        }
        //cout << r << endl;
        if(A.length() == n){
            int l= A.length();
            int to;
            cout << "First person at poisition " << A[r-1] << " is removed."<< endl;
            A.deleteElement(r,to);
            if(r == l){
                r = 1;
            }
        }
        else if(A.length() > 2){
            int l= A.length();
            int to;
            cout << "Then person at poisition " << A[r-1] << " is removed."<< endl;
            A.deleteElement(r,to);
            if(r == l){
                r = 1;
            }
        }
        else{
            int tmp;
            cout << "Finally, person at poisition " << A[r-1] << " is removed."<< endl;
            A.deleteElement(r,tmp);
        }
        r += k-1;
        //printList(A,0,A.length());    
    }
    cout << A[0] << " is the winner."<< endl;

}