#include<bits/stdc++.h>
using namespace std;

// the naive approach 
void findFactors(int n){
    vector<int>number;
    for(int i=1;i<n;i++){
        if(n%i==0){
            number.push_back(i);
        }
    }

    cout<<"Factors of "<<n<<" : ";
    for(auto &x : number){
        cout<<x<<" ";
    }

    // time complexity : O(n)
}

/*
Can we improve the above solution? 
If we look carefully, all the divisors are present in pairs. For example if n = 100, then the various pairs of divisors are: (1,100), (2,50), (4,25), (5,20), (10,10)
Using this fact we could speed up our program significantly. 
We, however, have to be careful if there are two equal divisors as in the case of (10, 10). In such case, we’d print only one of them. 
*/

// the effieict method
void printDivisors(int n){
    vector<int>number;
    number.push_back(1);
    for(int i=2;i<sqrt(n);i++){
        if(n%i==0){
            if(n/i==i){
                // if n/i gives the same number as i then, print only once
                cout<<i<<" ";
                number.push_back(i);
            }else{
                // else print the divisor and the quotient
                cout<<i<<" "<<n/i<<" ";
                number.push_back(i);
                number.push_back(n/i);
            }
        }
    }


    sort(number.begin() , number.end() );
    cout<<"\nPrinting the factors : ";
    for(auto &x : number){
        cout<<x<<" ";
    }

    cout<<"\n";
}

int main(){

    int n = 120;
    findFactors(n);
    cout<<"\n";
    printDivisors(n);


    return 0;
}