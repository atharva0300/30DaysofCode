def createStack(): 
    stack = []
    return stack 

def push(stack , x): 
    stack.append(x)

def pop(stack) :
    stack.pop()

def isEmpty(stack): 
    return len(stack)==0

def reverse(stack): 
    if isEmpty(stack): 
        return
    else  :
        print(stack.pop() , end=" ")
        return reverse(stack)

# Driver Code 
a = createStack()
push(a ,1)
push(a ,2)
push(a ,3)
push(a ,4)
push(a ,5)


reverse(a)
print()



