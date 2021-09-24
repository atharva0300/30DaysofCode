# Detect and remove loop in a linked list 
class Node : 
    def __init__(self , data): 
        self.data = data 
        self.next= None 

class LinkedList : 
    def __init__(self): 
        self.head = None 
    
    def PrintList(self) :
        temp = self.head 
        while(temp): 
            print(temp.data , end=" ")
            temp = temp.next 
        print()
    
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head =new_node 
    
    def append(self, new_data): 
        if self.head is None: 
            return 
        
        # else 
        temp = self.head 
        while(temp.next is not None ):
            temp = temp.next 
        
        new_node = Node(new_data)
        temp.next = new_node 
    
    def reverse(self): 
        if self.head.next is None: 
            return 
        
        # else 
        curr = self.head 
        prev = None 
        while(curr is not None ): 
            next = curr.next 
            curr.next= prev 
            prev= curr 
            curr = next 
        self.head = prev 
    
    def reverse_2(self , head ,k):
        if head is None : 
            return None
        
        # else 
        curr=  head
        prev = None 
        next = None 
        count =0
        while(curr is not None and count<k) :
            next = curr.next 
            curr.next = prev 
            prev= curr 
            curr = next 
            count = count +1 

        if next is not None: 
            head.next =self.reverse_2(next , k)
        
        return prev
    
    def detectAndRemoveLoop(self) : 
        slow_p = fast_p = self.head 

        while(slow_p and fast_p and fast_p.next ): 
            slow_p = slow_p.next 
            fast_p = fast_p.next.next

            #if slow_p and fast_p meet at some point then 
            # there is a loop
            if slow_p == fast_p: 
                self.removeLoop(slow_p)

                # Return 1 to indicate that the loop is found 
                return 1 
        # Return 0 to indicate that there is no loop
        return 0
    
    def removeLoop(self , loop_node ): 
        ptr1 = loop_node 
        ptr2 = loop_node 

        # count the number of nodes in the loop
        k = 1 
        while(ptr1.next !=ptr2): 
            ptr1 = ptr1.next
            k = k+1 
        
        # Fix one pointer to head 
        ptr1 = self.head 

        # And the other pointer is k nodes after head 
        ptr2 = self.head 
        for i in range(k) : 
            ptr2 = ptr2.next 
        
        # Move both pointers at the same place 
        # thet will meet at loop tarting node 
        while(ptr2!=ptr1): 
            ptr1 = ptr1.next 
            ptr2 = ptr2.next 
        
        # Get pointer to the last node 
        while(ptr2.next!=ptr1): 
            ptr2 = ptr2.next 
        
        ptr2.next = None 



def main()  :
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.append(4)
    llist.push(5)
    llist.append(6)
    llist.PrintList()
    llist.head = llist.reverse_2(llist.head , 3 )
    llist.PrintList()
    
    # Create a loop for testing 
    llist.head.next.next.next.next.next = llist.head.next.next 

    llist.detectAndRemoveLoop()

    print("Linked List after removing Loop :")
    llist.PrintList()



main()
