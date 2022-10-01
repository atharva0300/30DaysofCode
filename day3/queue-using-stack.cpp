#include<bits/stdc++.h>
using namespace std;

class Queue{
    stack<int>s1 , s2;

    void enQueue(int x){
        // move all the elements of the stack 1 to stack 2
        while(!s1.empty()){
            s2.push(s1.top());
            // adding the top element of the s1 stack into s2 stack

            // popping the stack1 top elemnet 
            s1.pop();
        }

        s2.push(x);
        // pushing the new element 

        while(!s2.empty()){
            // until s2 is not empty 
            // push all the elements of s2 to s1
            s1.push(s2.top());

            s2.pop();
        }

    }

    int deQueue(){
        // removing hte top most element of the s1 
        if(s1.empty()){
            cout<<"\nStack is empty";
            return -1;
        }else{
            int x = s1.top();
            // getting the top most element 
            s1.pop();
            // popping the top most element 

            return x;
        }
    }
};




int main(){


    return 0;
}