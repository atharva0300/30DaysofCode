#include<bits/stdc++.h>
using namespace std;

int main(){
    stack<int>myStack;

    myStack.push(12);
    myStack.push(11);
    myStack.push(9);
    myStack.push(14);

    // popping an element 
    myStack.pop();

    // printing all the elements of the stack 
    while(!myStack.empty()){
        cout<<myStack.top()<<" ";
        myStack.pop();
    }
    cout<<"\n";

    return 0;
}