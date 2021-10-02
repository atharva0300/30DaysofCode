# Next greater element using stack 

def createStack():
    stack = []
    return stack 

def isEmpty(stack): 
    return len(stack)==0

def push(stack ,x): 
    stack.append(x)

def pop(stack): 
    if isEmpty(stack):
        print("Stack is empty")
    else : 
        return stack.pop()

def PrintNGE(arr): 
    s= createStack()
    element =0
    next =0

    # push the first element to the stack 
    push(s, arr[0])


    # iterate for rest of teh elements 
    for i in range(1 , len(arr) , 1): 
        next= arr[i]

        if isEmpty(s)==False : 
            # if teh stack is not empty, then pop an element 
            # from the stack  
            element = pop(s)

            while(element<next ): 
                print(str(element) + " -- " +str(next))
                if isEmpty(s)==True: 
                    break
                element= pop(s)
            
            if element>next : 
                push(s ,element)

        push(s ,next)
    while isEmpty(s)==False: 
        element=pop(s)
        next= -1
        print(str(element) + " -- "  + str(next))


# Driver Code 
arr = [11,13,21,3]
PrintNGE(arr)
