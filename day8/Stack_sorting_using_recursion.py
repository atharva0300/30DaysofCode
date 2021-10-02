def sortedInsert(s , element ): 
    if len(s)==0 or element>s[-1] :
        s.append(element)
        return 
    else : 
        temp = s.pop()
        sortedInsert(s , element)
        s.append(temp)

def sortStack(s): 
    if len(s)!=0 :
        temp = s.pop()
        sortStack(s)
        sortedInsert(s , temp)

def printStack(s): 
    for i in s[::-1]: 
        print(i , end=" ")
    print()

# Driver Code 
s = []
s.append(30)
s.append(-5)
s.append(3)
s.append(10)
s.append(-12)
s.append(-23)

print("Stack elements before sorting : ")
printStack(s)

sortStack(s)

print("\nStack elements after sorting : ")
printStack(s)
