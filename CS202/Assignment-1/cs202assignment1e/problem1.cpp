#include <bits/stdc++.h>
#include "sorting.hpp"
#include "seqLinearList.hpp"

int m = 1000000007;

int main(){
    int n;
    cout << "Enter the length of Array: ";
    cin >> n;
    LinearList<float> A(n);
    cout << "Enter the Array: ";
    float x;
    for (int i = 0; i < n; i++)
    {
        cin >> x;

        A.insert(i+1,x);
    }

    int length = A.length();

    float meanA = 0;
    for (int i = 0; i < length; i++)
    {
        meanA += A[i];
    }
    
    meanA = meanA/length;

    float mn = abs(A[0]-meanA);

    for (int i = 0; i < n; i++)
    {
        if(mn > abs(A[i]-meanA)){
            mn = abs(A[i]-meanA);
        }
    }
    LinearList<float> L2(n);

    for (int i = 0; i < n; i++)
    {
        if(abs(A[i]-meanA) == mn){
            if(L2.search(A[i]) == 0){
                L2.insert(L2.length()+1,A[i]);
            }
        }
    }
    float sum = 0;
    for (int i = 0; i < L2.length(); i++)
    {
        sum += L2[i];
    }
    cout << "Answer: " << (int)sum%m  << endl;

}