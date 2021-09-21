# linked_list length iterative method 

class Node: 
    def __init__(self, data ): 
        self.data = data 
        self.next  = None 
    

class LinkedList: 
    def __init__(self): 
        self.head = None 

    # this function is in LinkedList class.it inserts 
    # a new node at the beginning od tthe linked list 
    def push(self , new_data ): 
        # 1 and 2 : allocate the node & 
        # put in the data 
        new_node  = Node(new_data)
        new_node.next  = self.head 

        
        # this functyion counts the number of nodes in the linkedlist 
        #$ iteratively, given 'node' as starting node 
    def getCount(self): 
        temp = self.head 
        # initialize the temp 
        count =0

        # looop while end of linkedlist is not found 
        while(temp ): 
            count = count +1 
            temp = temp.next 
        return count 
    
    def PrintList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data , end= " ")
            temp = temp.next 
        print()
        
    
def main() : 
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second 
    second.next = third 
    llist.PrintList()
    llist.push(12)
    print(llist.getCount())


main()
