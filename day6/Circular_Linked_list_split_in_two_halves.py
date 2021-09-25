# Split a circular linked liat in 2 halves 
class Node : 
    def __init__(self  , data ):
        self.data= data 
        self.next = None 

class CircularLinkedList : 
    def __init__(self) :
        self.head = None 

    def push(self , new_data) :
        ptr1 = Node(new_data)
        temp = self.head 

        ptr1.next = self.head 

        if self.head is not None : 
            while(temp.next!=self.head) :
                temp = temp.next 
            temp.next = ptr1
        else : 
            ptr1.next= ptr1 
        
        self.head = ptr1
    
    def PrintList(self ): 
        temp = self.head 
        if self.head is not None : 
            while(True) :
                print(temp.data , end=" ")
                temp = temp.next 
                if (temp ==self.head) : 
                    break
            print()
    
    def splitList(self , head1 , head2): 
        slow_ptr = self.head 
        fast_ptr = self.head 

        if self.head is None :
            return 
        
        # if there are odd nodes in the circular list then 
        # fast_ptr->next becomes and for even nodes 
        # fast_ptr->next->next becomes head 
        while(fast_ptr.next!=self.head and fast_ptr.next.next!=self.head)  :
            fast_ptr = fast_ptr.next.next 
            slow_ptr = slow_ptr.next 
        
        # If there are even elements in the list then 
        # move fast_ptr
        if fast_ptr.next.next==self.head : 
            fast_ptr = fast_ptr.next 
        
        # Set the head pointer of the first half 
        head1.head = self.head 

        #Set the head pointer of second half 
        if self.head.next !=self.head : 
            head2.head = slow_ptr.next 
        
        # Make second half circular 
        fast_ptr.next = slow_ptr.next 

        # Make firsthalf circular 
        slow_ptr.next = self.head


# Initialize lists as empty 
head = CircularLinkedList()
head1 = CircularLinkedList()
head2 = CircularLinkedList()

head.push(12)
head.push(56)
head.push(2)
head.push(11)

print("Original circular linked list")
head.PrintList()

#Split the list 
head.splitList(head1 , head2)

print("First circular Linked list")
head1.PrintList()

print("Second circular linked list ")
head2.PrintList()

