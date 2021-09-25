# Rotate a linked list 
class Node : 
    def __init__(self , data): 
        self.data=  data 
        self.next = None 

class LinkedList: 
    def __init__(self): 
        self.head = None 
    
    def PrintList(self) :
        temp = self.head 
        while(temp) :
            print(temp.data , end=" ")
            temp = temp.next 
        print()
    
    def push(self,new_data): 
        new_node = Node(new_data)
        new_node.next= self.head 
        self.head = new_node 
    
    def append(self, new_data): 
        if self.head is None :
            return
        
        # else 
        temp = self.head 
        while(temp.next is not None ): 
            temp = temp.next 
        
        new_node = Node(new_data)
        temp.next = new_node

    def rotate(self, k) :
        if k==0: 
            return 
        # else 
        current = self.head 
        count =1
        while(count<k and current is not None ) :
            current = current.next 
            count = count +1 
        
        if current is None : 
            return 

        kthnode = current

        while(current.next is not None ) :
            current = current.next 
        
        current.next = self.head 
        self.head = kthnode.next
        kthnode.next = None
    
    def rotate_2(head_ref, k) :
        if k==0: 
            return 
        
        #Let us understand the below 
        # code for example k=4 and 
        # list = 10.20.30.40.50.60
        current  = head_ref
        # traverse till the end
        while(current.next is not None ): 
            current = current.next 
        
        current.next = head_ref
        current = head_ref

        #traverse the linked list to k-1 
        # position which will be last element
        # for rotate array 
        for i in range(k-1 ): 
            current = current.next 
        
        # update the head_red and last 
        # element pointer to None 
        head_ref = current.next 
        current.next = None 
        return head_ref



    

def main(): 
    llist = LinkedList()
    for i in [1,4,2,6,4]: 
        llist.push(i)
    
    for i in [6,9,7,0]: 
        llist.append(i)
    
    llist.PrintList()
    llist.rotate(4)
    llist.PrintList()
    result = llist.rotate_2(llist.head, 4 )
    llist.PrintList()



main()