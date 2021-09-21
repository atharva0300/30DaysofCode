class Node: 
    def __init__(self , data) : 
        self.data = data 
        self.next = None 

class LinkedList: 
    def __init__(self): 
        self.head = None
    
    def PrintList(self) : 
        temp = self.head
        while(temp): 
            print(temp.data , end=" ")
            temp = temp.next 
        print()
        
    def delete(self, key):
        #store the head node 
        temp = self.head 

    # if head ndoe itself holds the key to be deleated 
        if (temp.data == key ): 
            self.head = temp.next 
            temp = None 
            return 
        
        # search for the key to eb deleated, keep track of the 
        # previous node as we need to change the 'prev_node'
        while(temp is not None ): 
            if temp.data ==key : 
                break
            prev = temp 
            temp = temp.next 
        
        # if the key was not present in the linkedlist 
        if (temp==None):
            return
        
        # unlink the node from the linked linkedlist 
        prev.next = temp.next 
        temp = None 



def main() : 
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second 
    second.next=  third 
    llist.PrintList()
    llist.delete(3)
    llist.PrintList()

main() 