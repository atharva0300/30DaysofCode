#include<bits/stdc++.h>
using namespace std;

class Node{
    public : 
        int data;
        Node* next;
};

void removeDuplicates(Node* head){
    Node* current = head;

    Node* next_next;
    if(current==NULL){
        return;
    }

    while(current->next!=NULL){
        if(current->data==current->next->data){
            next_next = current->next->next;
            free(current->next);
            // free the current->next from the memory
            current->next = next_next;
        }else{
        current = current->next;
        // else, just traverse the nodes
        }
    }

    
}


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

void checkPalindrome(Node* head){
    Node* temp = head;

    vector<int>v;
    while(temp!=NULL){
        v.push_back(temp->data);
        temp = temp->next;
    }

    // reverse traversing the vector
    int size = v.size();
    // printing the vector
    for(int i=size-1;i>=0;i--){
        cout<<v[i]<<" ";
    }

    size = v.size();
    int flag = true;
    temp = head;
    while(temp!=NULL){
        if(temp->data!=v[size-1]){
            flag = false;
            break;
        }
        temp = temp->next;
        size--;
    }

    if(flag==false){
        cout<<"\nNot a palindrome";
    }else{
        cout<<"\nA Palindrome";
    }
}

void removeDuplicatesFromUnsorted(Node* head){
    unordered_map<int , int>map;
    Node* temp = head;
    Node* next_next;

    map[temp->data]++;
    cout<<temp->data<<" : "<<map[temp->data]<<"\n";
    while(temp->next!=NULL){
        if(map[temp->next->data]==0){
            map[temp->next->data]++;
        }else if(map[temp->next->data]>=1){
            next_next  = temp->next->next;
            free(temp->next);
            temp->next = next_next;
        }

        cout<<temp->next->data<<" : "<<map[temp->next->data]<<"\n";
        temp = temp->next;
    }
}

void swapNodes(Node* head , int x  , int y){
    Node* temp = head;
    Node* prevX;
    Node* nodeX;
    Node* nextX;
    Node* prevY;
    Node* nextY;
    Node* nodeY;
    int count=0;

    while(temp!=NULL){
        if(count+1==x){
            prevX = temp;
            nodeX = temp->next;
            nextX = temp->next->next;
        }else if(count+1==y){
            prevY = temp;
            nextY = temp->next->next;
            nodeY = temp->next;
            prevX->next = nodeY;
            nodeY->next = nextX;

            prevY->next = nodeX;
            nodeX->next = nextY;
            
        }
        
        count++;
        temp = temp->next;
    }
}

void pairwiseSwampNodes(Node* head){
    Node* temp = head;

    while(temp!=NULL && temp->next!=NULL){
        swap(temp->data , temp->next->data);

        temp = temp->next->next;
    }
}

void moveLastElementToFront(Node* head){
    Node* temp = head;
    Node* lastNode;

    while(temp->next->next!=NULL){
        temp = temp->next;
    }

    lastNode = temp->next;
    cout<<"\nlast node : "<<lastNode->data<<"\n";
    temp->next = NULL;
    
    cout<<"\nlast node : "<<lastNode->data<<"\n";
    push(&head , lastNode->data);

    printList(head);
    
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
    push(&head , 12);
    cout<<"After insertion in the front : ";
    printList(head);

    removeDuplicates(head);
    cout<<"\nAfter removing duplicates : ";
    printList(head);

    checkPalindrome(head);
    cout<<"\n";

    push(&head , 12);
    push(&head , 2);
    cout<<"\nDisplaying the list before : ";
    printList(head);
    removeDuplicatesFromUnsorted(head);
    cout<<"\nLinked list after removing elements from unsorted list : ";
    printList(head);

    swapNodes(head , 1 , 3);
    cout<<"After Swapping nodes : ";
    printList(head);

    pairwiseSwampNodes(head);
    cout<<"\nAfter pariwise Swapping nodes : ";
    printList(head);

    moveLastElementToFront(head);
    cout<<"\nAfter moving the last element to the front : ";
    printList(head);

    return 0;
}