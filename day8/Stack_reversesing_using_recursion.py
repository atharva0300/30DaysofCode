def insertAtBottom(stack , item) :
    if isEmpty(stack) :
        push(stack , item)
    
    else : 
        temp = pop(stack)
        insertAtBottom(stack , item)
        push(stack , temp)

def reverse(stack) :
    if not isEmpty(stack) :
        temp =pop(stack)
        reverse(stack)
        insertAtBottom(stack , temp)

def createStack() :
    stack = []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack , item) :
    stack.append(item)

def pop(stack) :
    if isEmpty(stack) :
        print("Stack is empty")
    else : 
        return stack.pop()

def prints(stack) :
    for i in range(len(stack)-1, -1 , -1): 
        print(stack[i] , end=" ")
    print()


# Driver Code 
stack = createStack()
push(stack , str(4))
push(stack , str(5))
push(stack , str(6))
push(stack , str(7))
push(stack , str(8))
print("Original stack : ")
print(stack)

reverse(stack)

print("\nReversed stack : ")
print(stack)





