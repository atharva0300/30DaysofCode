# Linkedlist length recursive 
class Node: 
    def __init__(self , data) :
        self.data = data 
        self.next = None 


class LinkedList : 
    def __init__(self ): 
        self.head = None 
    
    def push(self , new_data): 
        new_node = Node(new_data)

        new_node.next = self.head 
        self.head = new_node
    
    def PrintList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data , end=" ")
            temp = temp.next 
        print()
    
    def getCount(self): 
        temp = self.head 
        count =0

        # Loop while the ned LinkedList is not found 
        while(temp) : 
            count = count +1 
            temp = temp.next 
        return count
    
    def getCountRec(self , temp): 
        if(not temp) : # Base case 
            return 0
        else : 
            return 1+ self.getCountRec(temp.next )
    
    def getCount_2(self): 
        return self.getCountRec(self.head)


def main()  :
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.PrintList()
    print(llist.getCount())
    print(llist.getCount_2())
    llist.push(12)
    llist.PrintList()
    print(llist.getCount())
    print(llist.getCount_2())


main()