# deleating a given node at a given position 
class Node: 
    def __init__(self ,data): 
        self.data = data
        self.next =None 


class LinkedList:
    def __init__(self): 
        self.head =None 
    
    def PrintList(self): 
        temp = self.head 
        while(temp) :
            print(temp.data , end=" ")
            temp = temp.next 
        print()
    
    def deleteNode(self, position):
        
        # if linkedlist is empty
        if self.head == None: 
            return 
        
        # store the head node 
        temp = self.head 

        #if the head needs to be removed 
        if position==0: 
            self.head = temp.next
            temp = None
            return 
        
        # find the previous node of the node to be deleated 
        for i in range(position - 1):
            temp = temp.next 
            if temp is None: 
                break
        
        # node temp.next is the node to be deleated 
        # store the pointer to the next of the node to be deleated 
        next = temp.next.next 
        
        # if position is more than the number of nodes 
        if temp is None : 
            return 
        if temp.next is None : 
            return

        # unlike the node from the linkedlist 
        temp.next =None 
        temp.next = next 
    



    

def main() :
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third 
    llist.PrintList()
    llist.deleteNode(1)
    llist.PrintList()



main()