# Circular Linked list 
class Node : 
    def __init__(self ,data): 
        self.data= data 
        self.next = None 

class CircularLinkedList : 
    def __init__(self):
        self.head = None  
    
    #This function is only for empty list 
    def addToEmpty(self, data): 
        if(self.head!=None ): 
            return self.head 
    
        # Creatng the newnode temp
        temp = Node(data)
        self.head = temp

        #Creating the link
        self.head.next = self.head 
        return self.head 
    
    def addBegin(self, data): 
        if(self.head==None) : 
            return self.addToEmpty(data)
        
        temp = Node(data)
        temp.next = self.head.next
        self.head.next = temp

        return self.head 
    
    def addEnd(self , data): 
        if(self.head ==None ) : 
            return self.addToEmpty(data)
        
        temp = Node(data)
        temp.next = self.head.next 
        self.head.next = temp
        self.head = temp
        return self.head 
    
    def addAfter(self, data , item) :
        if(self.head==None ): 
            return None 

        temp = Node(data)
        p  = self.head.next 
        while p :
            if (p.data==item) :
                temp.next  = p.next 
                p.next= temp

                if (p==self.head) :
                    self.head =temp
                    return self.head
                else : 
                    return self.head 
            
            p = p.next 
            if (p==self.head.next ): 
                print(item , "not present in the list ")
                break
        
    def traverse(self): 
        if (self.head == None ) :
            print("Listis empty ")
            return 
        
        temp = self.head.next 
        while(temp): 
            print(temp.data , end=" ")
            temp = temp.next 
            if temp==self.head.next : 
                break

def main() : 
    llist = CircularLinkedList()
    head= llist.addToEmpty(6)
    head= llist.addBegin(4)
    head= llist.addBegin(2)
    head= llist.addEnd(8)
    head= llist.addEnd(12)
    head= llist.addAfter(10,8)
    llist.traverse()
    print()


main()