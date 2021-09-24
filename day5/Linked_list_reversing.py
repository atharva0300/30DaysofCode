# Reversing a linked list 
class Node: 
    def __init__(self ,data): 
        self.data= data 
        self.next = None 
    

class LinkedList: 
    def __init__(self):
        self.head= None 
    
    def PrintList(self): 
        temp = self.head 
        while(temp) :
            print(temp.data , end=" ")
            temp = temp.next 
        print()
    
    def push(self , new_data): 
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head=  new_node
    
    def reverse(self): 
        prev =None 
        current = self.head 
        while(current ): 
            next = current.next 
            current.next = prev 
            prev= current 
            current = next 
        self.head= prev
    
    def reverse_2(self , head ) :
        # if head is empty or has reached the list end
        if(head is None or head.next is None) :
            return head 
        
        # reverse the rest lits 
        rest = self.reverse_2(head.next )

        # put the first element at the end 
        head.next.next = head 
        head.next  = None 

        # fix the header pointer 
        return rest 
    
    def __str__(self ): 
        lliststr= ""
        temp  =self.head 
        while(temp)  :
            lliststr = ( lliststr + str(temp.data) + " ")
            temp = temp.next 
        print()
        return lliststr
    
    def reverseUtil(self , curr , prev): 
        # if last node mark it head 
        if curr.next is None : 
            self.head= curr 

            # update next to prev node 
            curr.next = prev 
            return 
        
        # save curr.next node for recursive call 
        next =curr.next 

        # and update next 
        curr.next = prev 
        self.reverseUtil(next , curr)
        # This function mainly calls reverseUtil()
        # with previous as None 
    
    def reverse_3(self): 
        if self.head is None : 
            return
        self.reverseUtil(self.head , None)
    
    def reverseLLUsingStack(self,head): 
        # initialize the variables 
        stack , temp = [] , head 

        while(temp): 
            stack.append(temp)
            temp = temp.next 
        
        head= temp = stack.pop()

        # Untill stack is not 
        # empty 
        while(len(stack)>0): 
            elem = stack.pop()
            temp.next = elem
            temp = elem
        
        elem.next = None 
        return head 


def main() : 
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.PrintList()
    #llist.reverse_3()
    #llist.reverse_2()
    #llist.head = llist.reverse_2(llist.head)
    r = llist.reverseLLUsingStack(llist.head)
    while r: 
        print(r.data , end=" ")
        r = r.next
    llist.PrintList()
    



main()