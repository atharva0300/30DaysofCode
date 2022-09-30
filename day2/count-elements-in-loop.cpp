#include<bits/stdc++.h>
using namespace std;

class Node{
    public : 
        int data;
        Node* next;
};

void push(Node* head , int number){
    Node* newNode=  new Node();
    newNode->data = number;
    if(head==NULL){
        head = newNode; 
    }else{
        newNode->next = head;
        head= newNode;
    }
}

void printList(Node* head){
    Node* temp = head;
    while(temp!=NULL){
        cout<<temp->data<<" ";
        temp = temp->next;
    }
    cout<<"\n";
}

int countNodes(Node* n){
    int res = 1;
    Node* temp = n;
    while(temp->next!=n){
        res++;
        temp = temp->next;
    }

    return res;
}



int countNodesInLoop(Node* list){
    Node* slow_p = list;
    Node* fast_p = list;

    while(slow_p && fast_p && fast_p->next){
        slow_p = slow_p->next;
        fast_p = fast_p->next->next;


        if(slow_p==fast_p){
            return countNodes(slow_p);
        }
    }

    return 0;
}



int main(){

    Node* head = NULL;
    Node* second = NULL;
    Node* third = NULL;

    head = new Node();
    // allocating memory 
    second = new Node();
    third = new Node();

    head->next = second;
    second->next = third;

    head->data = 1;
    second->data = 2;
    third->data = 3;

    Node* temp = head;
    printList(temp);
    push(head , 12);
    cout<<"After insertion in the front : ";
    printList(head);

    cout<<countNodesInLoop(head)<<"\n"; 

    return 0;
}