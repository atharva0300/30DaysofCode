# Stack using Linkedlist 
class StackNode :
    # Constructor to initialize a node
    def __init__(self, data): 
        self.data = data
        self.next = next 

class Stack: 
    # Constructor to initialize the root of linekd list 
    def __init__(self): 
        self.head = None 
    
    def isEmpty(self): 
        return True if self.head is None else False 
    
    def push(self , data): 
        new_node = StackNode(data) 
        new_node.next=  self.head 

        self.head = new_node 
        print("{0} pushed to stack " .format(data))
    
    def pop(self): 
        if(self.isEmpty()) : 
            return float("-inf")
        
        temp = self.head
        self.head = self.head.next 
        popped=  temp.data
        return popped 
    
    def peek(self): 
        if self.isEmpty() :
            return float("-inf")
        
        return self.head.data

def main(): 
    stack = Stack() 
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("{0} popped from stack " .format(stack.pop()))
    print("Top element is {0} " .format(stack.peek()))



main() 

        