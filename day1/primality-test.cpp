#include<bits/stdc++.h>
using namespace std;


// the school method
bool isPrime(int n ){
    if(n<=1){
        return false;
    }

    for(int i=2;i<n;i++){
        if(n%i==0){
            return false;
        }
    }

    return true;

    // complexity => O(n)
}

// the optimized school method
bool isPrime2(int n ){
    if(n<=1){
        return false;
    }

    for(int i=2;i<=sqrt(n);i++){
        if(n%i==0){
            return false;
        }
    }

    return true;

    // complexity => O(sqrt(n))
}

/*
Another approach: It is based on the fact that all primes greater than 3 are of the form 6k ± 1, where k is any integer greater than 0. 
This is because all integers can be expressed as (6k + i), where i = −1, 0, 1, 2, 3, or 4. 
And note that 2 divides (6k + 0), (6k + 2), and (6k + 4) and 3 divides (6k + 3). 
So, a more efficient method is to test whether n is divisible by 2 or 3, then to check through all numbers of the form 6k ± 1 <= √n. 
This is 3 times faster than testing all numbers up to √n. (Source: wikipedia).  
*/
bool isPrime3(int n ){
    if(n==2 || n==3){
        return true;
    }

    if(n<=1 || n%2==0 || n%3==0){
        return false;
    }

    for(int i=5;i*i<=n;i+=6){
        if(n%i==0 || n%(i+2)==0){
            return false;
        }
    }

    return true;

    // time complexity : O(sqrt(n))
}


int main(){

    cout<<isPrime(25)<<"\n";
    cout<<isPrime(7)<<"\n";
    cout<<isPrime2(25)<<"\n";
    cout<<isPrime2(7)<<"\n";
    cout<<isPrime3(25)<<"\n";
    cout<<isPrime3(7)<<"\n";


    return 0;
}