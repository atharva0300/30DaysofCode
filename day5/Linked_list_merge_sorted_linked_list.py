# Linked list merging of sorted lists

class Node: 
    def __init__(self , data): 
        self.data = data 
        self.next =None 

class LinkedList: 
    def __init__(self): 
        self.head = None 
    
    def push(self , new_data): 
        new_node = Node(new_data)
        new_node.next=  self.head 
        self.head= new_node
    
    def PrintList(self): 
        temp =self.head 
        while(temp ): 
            print(temp.data , end=" ")
            temp = temp.next 
        print()

    def addToList(self , newData) : 
        newNode = Node(newData)
        if self.head is None :
            self.head = newNode
            return 
        
        last = self.head 
        while(last.next ): 
            last = last.next 
        
        last.next = newNode 
    
    def mergeLists(self, headA , headB) :

        # A dummy node to store the result 
        dummyNode = Node(0)

        # tail stotes the last node 
        tail = dummyNode
        while(True): 

            # If any of the list gets completely empty 
            # directly join all the elements of the other list 
            if headA is None : 
                tail.next = headB
                break
            if headB is None : 
                tail.next = headA 
                break
            # Comparethe data of the lists and whichever is smaller is 
            # appended to the ast of the merged list and head is 
            # changed 
            if headA.data <=headB.data: 
                tail.next = headA 
                headA = headA.next 
            else: 
                tail.next = headB 
                headB = headB.next 
            # Advance the tail
            tail = tail.next
        
        # Returns the head of the merged list 
        return dummyNode.next



listA =LinkedList()
listB = LinkedList()
# Add elements to listA 
listA.addToList(5) 
listA.addToList(10)
listA.addToList(15)

#Add elements to the list in sorted order for listB
listB.addToList(2)
listB.addToList(3)
listB.addToList(20)

# Call the merge function 
listA.head = listA.mergeLists(listA.head , listB.head)

# Display merged list 
print("Merged Linked list is : ")
listA.PrintList()
