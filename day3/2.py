count=0
start=0
end =0
class Queue() : 
    def create(): 
        l = []
        return l
    
    def push(l,a): 
        l.append(a)
        end =a
        return l
    
    def pop(l): 
        size = len(l)
        if size: 
            l.remove(l[end])
            return l
        return "Queue is empty"
    
    def empty(l) :
        return len(l)==0

def main() : 
    q = Queue
    l = q.create()
    print(q.push(l,12))
    print(q.empty(l))
    print(q.pop(l))
    print(q.empty(l))



main()