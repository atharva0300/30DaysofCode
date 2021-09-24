# Linked list merge sort 
class Node: 
    def __init__(self,  data): 
        self.data = data 
        self.next= None 

class LinkedList : 
    def __init__(self): 
        self.head = None 
    
    # push new elements to the list 
    def push(self , new_data): 
        new_node=  Node(new_data)
        new_node.next = self.head 
        self.head = new_node
    
    def PrintList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data , end=" ")
            temp = temp.next 
        print()
    
    def append(self , new_data): 
        # Allocate new node 
        new_node=  Node(new_data)

        #if head is None , initialixe it to new node 
        if self.head is None : 
            self.head = new_node
            return 
        
        curr_node  = self.head 
        while(curr_node.next ): 
            curr_node = curr_node.next 
        
        # Append the new_node to the end of the Linked list 
        curr_node.next = new_node

    def sortedMerge(self,  a , b): 
        result = None 

        # Base cases 
        if a==None: 
            return b 
        if b==None : 
            return a 
        
        # pick either a or b and recur :
        if a.data<=b.data: 
            result = a 
            result.next = self.sortedMerge(a.next , b)
        else : 
            result = b
            result.next = self.sortedMerge(a,  b.next )
        return result 
    
    def mergeSort(self , h): 
        # Base case if head is None 
        if h==None or h.next ==None : 
            return h 
        
        # get hte middle of the list 
        middle = self.getMiddle(h)
        nexttomiddle = middle.next 

        # Set the next of middle node to None 
        middle.next = None 

        # Apply mergeSort on left list 
        left = self.mergeSort(h)

        # Apply merge sort on the right list 
        right = self.mergeSort(nexttomiddle )

        # Merge the left and right lists 
        sortedlist = self.sortedMerge(left, right )
        return sortedlist
    
    # Utility function 
    # getMiddle 
    def getMiddle(self , head ): 
        if (head ==None ): 
            return head 
        
        slow= head 
        fast = head 
        while(fast.next !=None and fast.next.next!=None): 
            slow = slow.next 
            fast = fast.next.next 
        return slow 
    
    def getmiddle_myself(self): 
        if self.head is None : 
            return self.head 
        
        slow = self.head 
        fast = self.head 
        while(slow.next!=None and fast.next.next!=None): 
            slow= slow.next 
            fast =  fast.next.next 
        return slow

def main(): 
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.append(4)
    llist.PrintList()

    #getmiddle_myself
    result= llist.getmiddle_myself()
    print(result.data)

    # Apply merge sort 
    llist.head = llist.mergeSort(llist.head)
    print("Sorted Linked List : ")
    llist.PrintList()




main()