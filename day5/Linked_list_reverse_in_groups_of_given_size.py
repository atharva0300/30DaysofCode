# Reverse a likned list in groupsof given size 
class Node: 
    def __init__(self , data): 
        self.data= data 
        self.next = None 

class LinkedList : 
    def __init__(self) :
        self.head = None 
    
    def PrintList(self) : 
        temp = self.head 
        while(temp) :
            print(temp.data , end=" ")
            temp = temp.next 
        print()

    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head= new_node 
    
    def append(self , new_data): 
        if self.head is None : 
            return self.head 
        
        # else 
        temp = self.head 
        while(temp.next is not None ): 
            temp =temp.next 
        
        new_node = Node(new_data)
        temp.next = new_node 
    
    def reverse(self) :
        if self.head.next is None : 
            return 
        curr = self.head 
        prev = None 
        while(curr is not None):
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        self.head= prev 
    
    def reverse_2(self , head , k): 
        if head ==None : 
            return None 
        
        current = head 
        next = None 
        prev = None 
        count =0

        # Reverse first k nodes of the Linked list 
        while(current  is not None and count<k) :
            next = current.next 
            current.next = prev
            prev=  current 
            current = next 
            count = count +1
        
        # next is now a pointer to ( k+1 )th node 
        # recursively call for the list starting 
        # from the current. And make the rest of the list as 
        # next to first Node
        if next is not None : 
            head.next = self.reverse_2(next , k)
        
        # prev is new head of the input list 
        return prev 


def main() : 
    llist  = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.append(4)
    llist.append(5)
    llist.push(6)
    llist.push(7)
    llist.push(8)
    llist.PrintList()
    llist.head_2 = llist.reverse()
    '''
    llist.head = Node(1)
    second= Node(2)
    third = Node(3)
    llist.head.next= second 
    second.next = third 
    '''
    
    llist.PrintList()
    llist.head = llist.reverse_2(llist.head ,3)
    llist.PrintList()


main()
