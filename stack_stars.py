'''def remove_stars(s: str) -> str:
    stack = []
    
    for char in s:
        if char == '*':
            if stack:
                stack.pop() 
        else:
            stack.append(char)
    
    return ''.join(stack)
input_string = "leet**cod*e"
result = remove_stars(input_string)
print(result) '''
a="leet**co*de"
b=[]
for i in a:
    if(i !='*'):
        b.append(i)
    else:
        b.pop()
print(''.join(b))
