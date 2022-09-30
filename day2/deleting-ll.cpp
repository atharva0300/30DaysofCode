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
    newNode->next = *head_ref;

    // making the newNode as the head node 
    (*head_ref) = newNode;

}

void deleteLLFromFront(Node** head_ref){
   if(*head_ref==NULL){
        return;
   }else{
         Node* temp = *head_ref;

        *head_ref = (*head_ref)->next;
        free(temp);


        return deleteLLFromFront(head_ref);
   }

}

void deleteLLFromLast(Node** head_ref){
    Node* temp = *head_ref;
    while(temp->next->next!=NULL){
        temp = temp->next;
    }

    temp->next = NULL;
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

    push(&head , 12);
    push(&head , 100);
    printList(head);

    deleteLLFromFront(&head);
    cout<<"Displaying the list after deleting from the front : "; 
    printList(head);

    return 0;
}