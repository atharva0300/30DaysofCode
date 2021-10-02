def createStack(): 
    stack = []
    return stack

def push(stack , x): 
    stack.append(x)

def pop(stack): 
    if isEmpty(stack)==0: 
        print("Stack is empty")
    else : 
        e = stack.pop()
        return e

def isEmpty(stack): 
    return len(stack)==0

def reverse(stack ,size): 
    temp = []
    for i in range(0 , size): 
        if isEmpty(stack):
            break
        else : 
            temp.append(stack.pop())
    return temp
    

# Driver Code 
arr = createStack()
push(arr, 1)
push(arr, 2)
push(arr, 3)
push(arr, 4)

print("Original stack")
print(arr)


print("\nReversed stack : ")
print(reverse(arr ,len(arr)))

