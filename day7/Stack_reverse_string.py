# Reverse a string using stack 
def createStack(): 
    stack = []
    return stack
# Function to determine the size of the stack 
def size(stack): 
    return len(stack)

# Stack is empty if the size of 0
def isEmpty(stack) :
    if size(stack)==0: 
        return True

# Function to add an item to stack 
# it increases size by 1 
def push(stack , item) : 
    stack.append(item)

# Function to remove an item from stack
# it increases size by 1 
def push(stack , item) :
    stack.append(item)

# Function to remove the item from the stack 
# it decreases the size by 1 
def pop(stack ): 
    if isEmpty(stack): 
        return 
    return stack.pop()

# A stack based function to reverse a string
def reverse(string): 
    n = len(string )

    # Create an empty stack 
    stack = createStack()

    #push all the characters of string to stack
    for i in range(0 , n , 1): 
        push(stack , string[i])
    
    # making the string mepty since all
    # characters are saved to string 
    for i in range(0 , n , 1): 
        string = string + pop(stack)
    
    return string 

# Driver program to test the above code
string = "AtharvaPingale\n"
string = reverse(string)
print(string)
