# Linked list isertion
class Node: 
    def __init__(self , data ): 
        self.data = data 
        self.next = None 


class LinkedList: 
    def __init__(self ): 
        self.head= None 
    
    def PrintList(self): 
        temp = self.head 
        while(temp ):
            print(temp.data , end=" ")
            temp = temp.next 
        print()
    
    def push(self,new_data): 
        new_node= Node(new_data)
        new_node.next =self.head 
        self.head = new_node 
    
    def insertAfter(self, prev_node,  new_data): 
        if prev_node is None: 
            print("The given previous node must in LinkedList")
            return 
        new_node = Node(new_data )
        new_node.next = prev_node.next 
        prev_node.next = new_node 
    
    def append(self ,new_data) :
        new_node = Node(new_data)

        # if the linkedlist is empty 
        if self.head is None : 
            self.head= new_node
            return 
        
        # else traverse the entire list 
        last = self.head 
        while(last.next ) : 
            last = last.next
        
        # change the next node of teh last node 
        last.next = new_node 

        


        

def main() : 
    llist = LinkedList() 
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next =third 
    llist.PrintList()
    llist.push(12)
    llist.PrintList()
    llist.insertAfter(llist.head.next,34)
    llist.PrintList()
    llist.append(90)
    llist.PrintList()


main() 