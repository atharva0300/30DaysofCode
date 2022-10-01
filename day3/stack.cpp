#include<bits/stdc++.h>
using namespace std;

#define MAX 1000
// defining the maximum length of the stack as 1000

class Stack{
    int top;

    public : 
        int a[MAX];
        // maximum size of the stack;

        Stack(){
            top = -1;
        }

        bool push(int x);
        int pop();
        int peek();
        bool isEmpty();
};

bool Stack::push(int x){
    if(top>=(MAX-1)){
        cout<<"Stack Overflow\n";
        return false;
    }else{
        a[++top] = x;
        cout<<x<<" pushed into stack";
        return true;
    }
}

int Stack::pop(){
    if(top<0){
        cout<<"Stack overflow";
        return 0;
    }else{
        int x = a[top--];
        return x; 
    }
}

int Stack::peek(){
    if(top<0){
        cout<<"Stack is empty";
        return 0;
    }else{
        int x = a[top];
        // getting the top element of the stack
        return x;
    }
}

bool Stack::isEmpty(){
    // returning is the stack is empty or not 
    return (top<0);
}

int main(){
    class Stack s;
    s.push(10);
    s.push(20);
    s.push(30);

    cout<<s.pop()<<" popped from the stack\n";

    cout<<"top element is : "<<s.peek()<<"\n";

    cout<<"\nElement present in the stack : ";
    while(!s.isEmpty()){
        cout<<s.peek()<<" ";
        s.pop();
    }
    cout<<"\n";

    return 0;
}
