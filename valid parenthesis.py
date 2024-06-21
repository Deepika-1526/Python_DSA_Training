'''n = input("Enter the string: ")

def valid_parenthesis(s):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for i, c in enumerate(s):
        if c in opening_brackets:
            stack.append((c, i))
        elif c in closing_brackets:
            if stack and stack[-1][0] == matching_bracket[c]:
                stack.pop()
            else:
                return i + 1  
    
    if stack:
        return stack[-1][1] + 1  
    
    return -1  

res = valid_parenthesis(n)
print(res)'''
