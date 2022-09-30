#include<bits/stdc++.h>
using namespace std;

class Node{
    public : 
        int data;
        Node* next;

};

void push(Node** head_ref , int number){
    Node* newNode = new Node();

    newNode->data = number;
    newNode->next = *head_ref;

    // making the newNode as the head node 
    (*head_ref) = newNode;

}

void printList(Node* temp){
    while(temp!=NULL){
        cout<<temp->data<<" ";
        temp = temp->next;
    }
    cout<<"\n";
}


int nthNode(Node* temp , int index){
    int count=0;
    while(temp!=NULL && count!=index){
        temp = temp->next;
        count++;
    }

    return temp->data;
}

int Getsize(Node* temp){
    int count=0;
    while(temp!=NULL){
        temp = temp->next;
        count++;
    }

    return count;
}


int nthNodeFromEnd(Node* temp , int index){
    int count=0;
    int size = Getsize(temp);
    int position = (size-index)-1;
    while(temp!=NULL && count!=position){
        temp = temp->next;
        count++;
    }

    return temp->data;
}

int printMiddle(Node* temp){
    int size = Getsize( temp);
    int middle = floor(size/2);
    int count=1;
    while(temp!=NULL && count!=middle){
        temp = temp->next;
        count++;
    }

    return temp->data;
}


int countOccurence(Node* temp , int number){
    int count=0;
    while(temp!=NULL){
        if(temp->data==number){
            count++;
        }
        temp = temp->next;
    }

    return count;
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

    int index =2;
    cout<<nthNode(head , index)<<"\n";
    cout<<nthNodeFromEnd(head , index)<<"\n";

    cout<<printMiddle(head)<<"\n";
    push(&head , 2);
    cout<<"occurence of 2 : "<<countOccurence(head , 2)<<"\n";
    

}