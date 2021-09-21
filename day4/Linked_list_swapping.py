# Linked_list swapping 

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
    

class LinkedList : 
    def __init__(self): 
        self.head = None 
    
    def PrintList(self): 
        temp = self.head 
        while(temp) :
            print(temp.data , end=" ")
            temp = temp.next 
        print()
    
    def push(self  , new_data):
        new_node = Node(new_data)
        new_node.next  = self.head 
        self.head = new_node
    
    def swap(self , x , y): 

        # Nothing to do if x and y are same 
        if(x==y): 
            return 
        
        # Search for x ( keep track of prevX and CurrX)
        prevX = None
        currX = self.head 
        while currX !=None and currX.data!=x: 
            prevX = currX 
            currX = currX.next
        
        prevY = None 
        currY = self.head 
        while currY!=None and currY.data!=y : 
            prevY = currY
            currY = currY.next 
        
        # if either x or y is not present, nothing to do
        if currX==None or currY==None :
            return 
        
        if prevX!=None : 
            prevX.next = currY
        else: 
            self.head = currY
        
        # if y is not head of linkedlist 
        if prevY!=None :
            prevY.next = currX 
        else : 
            self.head = currX 
        
        # Swap next pointers 
        temp = currX.next 
        currX.next = currY.next 
        currY.next = temp


def main() : 
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.PrintList()
    llist.swap(4,3)
    llist.PrintList()

main()


