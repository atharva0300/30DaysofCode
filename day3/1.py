class Stack() : 
    def create(): 
        l = []
        return l
        
    def empty_list(l) :
        return len(l)!=0

    def push(l,a) :
        l.append(a)
        return l

    def pop(l,a):
        b = len(l)
        if(b): 
            l.remove(a)
            return l
        return "Stack is empty"




def main(): 
    s = Stack
    l = s.create()
    print(s.push(l,12))
    print(s.empty_list(l))
    print(s.pop(l,12))
    print(s.empty_list(l))
    print(s.pop(l,13))


main()