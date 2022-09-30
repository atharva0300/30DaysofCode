#include<bits/stdc++.h>
using namespace std;

class Node{
    public : 
        int data;
        Node* next;

};



void printList(Node* temp){
    while(temp!=NULL){
        cout<<temp->data<<" ";
        temp = temp->next;
    }
    cout<<"\n";
}

void push(Node** head_ref , int number){
    Node* newNode = new Node();

    newNode->data = number;

    if(*head_ref==NULL){
        // make the new node as the head node
        *head_ref = newNode;
    }else{
        newNode->next = *head_ref;

        // making the newNode as the head node 
        (*head_ref) = newNode;
    }

    cout<<"head_ref data : "<<(*head_ref)->data<<"\n";


} 

void append(Node* head , int number){
    Node* newNode= new Node();
    newNode->data =number;
    if(head==NULL){
        head = newNode;
    }else{
        Node* temp = head;
        while(temp->next!=NULL){
            temp = temp->next;
        }

        temp->next = newNode;
    }
}

void segregateOddEven(Node* head){
    Node* temp = head;
    Node* next_next;
    Node* next_next_next;

    Node* even = NULL;
    Node* odd = NULL;

    even = new Node();
    odd = new Node();

    Node* evenLast;



    while(temp!=NULL){
        if((temp->data)%2==0){
            // push in the even ll
            append(even , temp->data);
            evenLast = temp;
        }else{
            append(odd , temp->data);
        }

        temp = temp->next;
    }

    // joing the end of the even list with the start of the odd list
    cout<<"even last : "<<evenLast->data<<"\n";
    cout<<"odd : "<<odd->data<<"\n";
    cout<<"odd next : "<<odd->next->data<<"\n";

    evenLast->next = odd;

    cout<<"even : "<<even->data<<"\n";
    cout<<"\nList after segregating : ";
    printList(even);
}

void reverseLinkedList(Node* head){
    Node* current= head;
    Node* prev=  NULL;
    Node* next = NULL;

    while(current!=NULL){
        // store the next
        next = current->next;

        // reverse the current node's pointer
        current->next = prev;

        // move the pointers one position ahead
        prev = current;
        current = next;
    }

    head = prev;

}

void recursivePrintReverseLinkedList(Node* head){
    if(head==NULL){
        return;
    }

    recursivePrintReverseLinkedList(head->next);

    cout<<head->data<<" ";
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
    push(&head , 12);
    cout<<"After insertion in the front : ";
    printList(head);

    //segregateOddEven(head);

    reverseLinkedList(head);

    Node* t = head;
    cout<<"\nLinked list after reversing : ";
    printList(head);
    cout<<"\nrecursively print reverse Linekd list : ";
    recursivePrintReverseLinkedList(head);
    cout<<"\n";


    return 0;
}