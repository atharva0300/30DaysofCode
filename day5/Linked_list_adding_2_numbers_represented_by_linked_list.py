# Add 2 numbers represented by linked list 
class Node: 
    def __init__(self , data): 
        self.data = data
        self.next = None 

class LinkedList : 
    def __init__(self): 
        self.head = None 
    
    def PrintList(self ): 
        temp = self.head 
        while(temp) :
            print(temp.data ,end=" ")
            temp = temp.next 
        print() 
    
    def push(self , new_data) : 
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node
    
    def append(self , new_data): 
        if self.head is None : 
            return 
        
        # else 
        temp = self.head 
        while(temp.next is not None ):
            temp = temp.next 
        
        new_node = Node(new_data)
        temp.next = new_node 
    
    def reverse(self) :
        if self.head is None : 
            return 
        
        # else 
        curr = self.head
        prev= None 
        while(curr is not None ): 
            next= curr.next 
            curr.next = prev
            prev=  curr 
            curr = next 
        self.head= prev 
    
    def length(self) :
        count =0
        temp = self.head 
        while(temp) : 
            temp = temp.next 
            count = count +1 
        return count 
    
    def length_2(self , head): 
        if (not head):
            return 0
        else: 
            return 1 + self.length_2(head.next)
    
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
    
    def addTwoLists(self,first, second ): 
        prev  =None 
        temp = None 
        carry =0

        #While both lists exists 
        while(first is not None or second is not None ): 
            # Calculate the value of the next digit in 
            # Resultant list 
            # The next digit is the sum of teh followting thigs 
            # (i) Next digit of the first list ( if iter is a next digit ) 
            # (iii) next digit of second list ( if there is a next digit )
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata

            # update carry for next calculation 
            carry = 1 if Sum>=10 else 0

            # update sum if it is greate than 10
            Sum = Sum if Sum <10 else Sum %10

            #create a new node with the sum as data 
            temp = Node(Sum)

            #If this is the first node then set it as head 
            # of resulant list 
            if self.head is None : 
                self.head = temp
            else  :
                prev.next  = temp
            
            # set prev for next insertio 
            prev = temp

            # Move first and second pointers to next nodes 
            if first is not None : 
                first = first.next 
            if second is not None : 
                second = second.next 
            
            if carry>0 :
                temp.next = Node(carry)



def main() : 
    llist =LinkedList()
    llist.push(1)
    llist.push(2)
    llist.append(3)
    llist.PrintList()
    llist.reverse()
    llist.PrintList()
    print(llist.length())
    print(llist.length_2(llist.head))
    llist.swap(2,3)
    llist.PrintList()
    llist2 = LinkedList()
    llist2.push(1)
    llist2.append(2)
    llist2.push(3)
    llist2.PrintList()
    res = LinkedList()
    res.addTwoLists(llist.head , llist2.head)
    res.PrintList()



main()