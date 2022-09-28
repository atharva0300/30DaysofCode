#include<bits/stdc++.h>
using namespace std;

void sieveOfErasthones(int n ){
    bool prime[n+1];
    memset(prime , true , sizeof(prime));
    // setting all the values of prim to true

    for(int p=2;p*p<=n;p++){
        if(prime[p]==true){
            for(int i=p*p;i<=n;i+=p){
                prime[i] = false;
            }
        }
    }


    // print all prime numbers
    for(int p=2;p<=n;p++){
        if(prime[p]){
            cout<<p<<" ";
        }
    }

    // Time Complexity: O(n*log(log(n)))
}

int main(){
    int n = 30;
    sieveOfErasthones(30);
    cout<<"\n";

    return 0;
}