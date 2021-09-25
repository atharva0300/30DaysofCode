# Rotate linked list 
class Node: 
    def __init__(self , data): 
        self.data = data
        self.next = None 

class LinkedList : 
    def __init__(self): 
        self.head = None 
    
    def PrintList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data,  end=" ")
            temp = temp.next 
        print()
    
    def push(self , new_data): 
        new_node=  Node(new_data)
        new_node.next = self.head 
        self.head = new_node
    
    def append(self , new_data): 
        if self.head is None: 
            return 
        temp = self.head 
        while(temp.next!=None):
            temp = temp.next 
        
        new_node = Node(new_data)
        temp.next = new_node 
    
    def rotate(self, k): 
        if k==0: 
            return 
        
        # Let us uderstad the below code for example k = 4 
        # and list = 10->20->30->40->50->60
        current = self.head 

        # current will either point to kth or NULLL after 
        # this loop
        # current will point to node 40 in the above example 
        count =1 
        while(count<k and current is not None ): 
            current = current.next 
            count = count +1 
        
        # If current is None, k is greater than or equal 
        # to count of nodes is Linked List. Don't change 
        # the list in this case 
        if current is None : 
            return 
        
        # current points to kth node. Store it in a variable 
        # kth node points to node 40 in the above example
        kthnode = current 
        # current will point ti the last node afer this loop
        # current will point to node 60 in the above example 
        while(current.next is not None ): 
            current = current.next 
        
        # Change next of last node to previous head 
        #Next of 60 is nw changed to node 10 
        current.next = self.head 

        #change head to ( k+1 )th node 
        # head is not changed to node 50 
        self.head= kthnode.next

        # Change next of kth node to NULL
        # next of 40 is not NULL
        kthnode.next = None 


def main() : 
    llist = LinkedList()
    for i in [1,3,2,5,4]: 
        llist.push(i)
    
    for i in [8,7,10,9]: 
        llist.append(i)
    llist.PrintList()
    llist.rotate(4)
    llist.PrintList()





main() 
