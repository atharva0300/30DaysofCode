# Reverse a Doubly Linked list 
class Node : 
    def __init__(self, data): 
        self.data =data 
        self.next= None 
        self.prev= None 

class DoublyLinkedList  :
    def __init__(self ): 
        self.head = None
    
    def push(self ,new_data): 
        
        new_node=  Node(new_data)
        new_node.next= self.head 
        
        if self.head is not None :
            self.head.prev = new_node 
        
        self.head=  new_node
    
    def printList(self , node):
        while(node is not None ):
            print(node.data , end=" ")
            node = node.next 
        print()
    
    def append(self ,new_data):
        if self.head is None or new_data is None : 
            return 
        
        new_node = Node(new_data)
        
        if self.head.next is None : 
            self.head.next = new_node 
            new_node.prev=  self.head
        else  :
            # traverse the list 
            node = self.head 
            while(node.next is not None ) :
                node = node.next 
            
            node.next= new_node
            new_node.prev = node
    
    def reverse(self): 
        temp = None 
        current =self.head 

        # Swap next and the prev for all nodes of 
        # dounbly linked list 
        while current is not None : 
            temp = current.prev
            current.prev= current.next 
            current.next = temp
            current = current.prev
        
        # Before changing head, check for the cases like 
        #empty list and lit, with only one node 
        if temp is not None: 
            self.head = temp.prev 
    
    def reverseUsingStacks(self): 
        stack = []
        temp =self.head 
        while temp is not None :
            stack.append(temp.data)
            temp = temp.next 
        
        # Add all the elements in the stack
        # in a esquence to the stack 
        temp = self.head 
        while temp is not None : 
            temp.data = stack.pop()
            temp = temp.next 
        
        # poppeed all the eleents and then 
        # added in the linked list 
        # in the reverse order 


    


def main() :
    dll = DoublyLinkedList()
    dll.push(1)
    dll.push(3)
    dll.printList(dll.head)
    dll.append(4)
    dll.printList(dll.head)
    #dll.reverse()
    dll.reverseUsingStacks()
    dll.printList(dll.head )


main()