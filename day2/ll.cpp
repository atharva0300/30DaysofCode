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

void insertAtPosition(Node** head_ref , int position , int number){
    // creating a new node 
    Node* newNode=  new Node();
    newNode->data = number;
    Node* temp = *head_ref;
    //creating a temp node which point to the head

    int count=0;
    while(temp!=NULL && count+1!=position){
        temp = temp->next;
        count++;
    }

    //storing the next of the temp
    Node* temp2 = temp->next;
    temp->next = newNode;
    newNode->next = temp2;

}

void append(Node** head_ref , int number){
    // creating a new node 
    Node* newNode = new Node();
    newNode->data = number;
    if(*head_ref==NULL){
        *head_ref = newNode;
        return;
    }

    // creating A TEMP node 
    Node* temp = *head_ref;

    while(temp->next!=NULL){
        temp = temp->next;
    }

    // getting the the last node of the linked list 
    // inserting the node at the last 
    temp->next = newNode;
}

void deleteFront(Node** head_ref){
    if(*head_ref == NULL){
        return;
    }
    
    // storing the head node to a temp varible 
    Node* temp = *head_ref;
    Node* temp2 = temp->next;
    temp->next = NULL;
    *head_ref = temp2;

}

void deleteLast(Node** head_ref){
    // creating a temp node which is pointing to the head node 
    Node* temp = *head_ref;
    while(temp->next->next!=NULL){
        temp = temp->next;
    }

    temp->next = NULL;
}

void deleteAtPosition(Node** head_ref , int position){
    Node* temp = *head_ref;
    int count=0;

    while(temp!=NULL && count+1!=position){
        temp = temp->next;
    }

    // getting the next node of the temp node
    Node* temp2 = temp->next;
    Node* temp3 = temp->next->next;
    temp->next = NULL;
    temp2->next = NULL;
    temp->next = temp3;
}

int lengthLL(Node** head_ref){
    Node* temp = *head_ref;
    int count=0;
    // iterative method
    while(temp!=NULL){
        temp = temp->next;
        count++;
    }

    return count;
}

int lengthLL2(Node** head_ref , int count){
    if(*head_ref==NULL){
        return count;
    }else{
        *head_ref = (*head_ref)->next; 
        count++;
        return lengthLL2(head_ref , count);
    }
}

int searchLL(Node* temp , int number){
    int position = 0;
    int index =0;
    while(temp!=NULL){
        if(temp->data==number){
            position = index;
            cout<<"index : "<<index<<"\n";
            break;
        }
        cout<<temp->data<<"\n";
        index++;
        temp = temp->next;
    }

    return position;
}

int searchLL2(Node* temp , int number , int position){
    if(temp==NULL){
        return -1;
    }else if(temp->data==number){
        return position;
    }else{
        position++;
        temp = temp->next;
        return searchLL2(temp , number , position);
    }
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

    insertAtPosition(&head , 2 , 100);
    printList(head);

    append(&head , 99);
    printList(head);

    deleteFront(&head);
    printList(head);

    deleteLast(&head);
    printList(head);

    //deleteAtPosition(&head , 2);
    //printList(head);

    cout<<lengthLL(&head)<<"\n";
    cout<<lengthLL2(&head , 0)<<"\n";

    printList(head);
    append(&head , 1);
    append(&head , 2);
    append(&head , 3);
    append(&head , 4);
    printList(head);

    cout<<"Index of the elemnet : "<<searchLL(head ,2)<<"\n";
    cout<<"index of the element : "<<searchLL2(head , 2 , 0)<<"\n";


    return 0;
}