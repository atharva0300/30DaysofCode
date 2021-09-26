# Doubly linked list 
class Node : 
    def __init__(self ,next = None , prev = None , data=None ): 
        self.next = next # Reference to the next node in DLL
        self.prev = prev # Reference to previous node in DLL
        self.data = data

def push(self, new_data ): 

    #1 ad 2 : allocate the node and put i the data 
    new_node = Node(data = new_data)

    # 3. Mkae next of new node as head and previous as NULL
    new_node.next = self.head 
    new_node.prev = None 

    # 4. Change prevof head node to new node 
    if self.head is not None : 
        self.head.prev = new_node
    
    # 5. Move the head to point to the new node 
    self.head = new_node 

def insertAfter(self , prev_node, new_data) :
    # 1.Check if the given prev_node is NULL 
    if prev_node is None : 
        print("This node dosen't exist in DLL ")
        return 
    
    # 2. Allocate node & 3. put in the data 
    new_node = Node(data = new_data)

    # 4.make next of the new node as the next of trhe prev_node 
    new_node.next = prev_node.next 

    #5. Make the next of the prev_node as new_node 
    prev_node.next = new_node 

    #6.  Make prev_node as previous of new_node 
    new_node.prev = prev_node 

    # 7. Change previous of new node's next node 
    if new_node.next is not None : 
        new_node.next.prev = new_node

def append(self, new_data) : 
    # 1. allocate node 2. put in the data 
    new_node = Node(data= new_data)
    last= self.head 

    # 3. this new ndoe is goig to be the 
    # last node, so mkae next of it as NULL
    new_node.next = None 

    # 4. If the linked list is empty, then 
    # make the new node as head 
    if self.head is None : 
        new_node.prev= None 
        self.head = new_node
        return 
    
    # 5. Else traverse till the last node 
    while(last.next is not None ) :
        last = last.next 
    
    # 6. change the next of teh last node 
    last.next = new_node 

    # 7. make the last node as previous of the new node 
    new_node.prev = last

def push_2(head_ref, new_data):
 
    # /* 1. allocate node */
    new_node = Node(new_data)
 
    # /* 2. put in the data */
    new_node.data = new_data
 
    # /* 3. Make next of new node as
    # head and previous as None */
    new_node.next = head_ref
    new_node.prev = None
 
    # /* 4. change prev of head node to new node */
    if (head_ref != None):
        head_ref.prev = new_node
 
    # /* 5. move the head to point to the new node */
    head_ref = new_node
 
    return head_ref
 
# /* Given a node as next_node, insert
# a new node before the given node */

def insertBefore(head_ref, next_node, new_data):
 
    # /*1. check if the given next_node is NULL */
    if (next_node == None):
        print("the given next node cannot be NULL")
        return
 
    # /* 3. put in the data */
    new_node = Node(new_data)
 
    # /* 4. Make prev of new node as prev of next_node */
    new_node.prev = next_node.prev
 
    # /* 5. Make the prev of next_node as new_node */
    next_node.prev = new_node
 
    # /* 6. Make next_node as next of new_node */
    new_node.next = next_node
 
    # /* 7. Change next of new_node's previous node */
    if (new_node.prev != None):
        new_node.prev.next = new_node
 
    # /* 8. If the prev of new_node is NULL, it will be
    #   the new head node */
    else:
        head_ref = new_node
 
    return head_ref
 
# This function prints contents of linked
# list starting from the given node

def printList(node ) : 
    last = None 
    print("Traversal in forward direction ")
    while(node!=None  ) :
        print(node.data , end=" ")
        last=  node 
        node = node.next 
    
    print("\nTraversal in reverse direction ")
    while(last!=None ) :
        print(last.data, end=" ")
        last= last.prev

def main( ) :
    head = None 
    head = push_2(head , 7 )
    head = push_2(head ,1 )
    head = push_2(head , 4 )

    # insert 8 , before 1. So linked list becomes 4.8.1.7.NULL
    head = insertBefore(head ,head.next , 8)
    print("Created DLL is  : ")
    printList(head)
    print()



main()



    



    

