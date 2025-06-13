s1 = "()[]{}"
s2 = "(]"

map = {'(':')','[':']','{':'}'}

stack = [None] * len(s1)
top = -1

for c in s1:
    if c in map:
        top += 1
        stack[top] = c
    else:
        if top == -1:
            print(False)
            break
        opening = stack[top]
        if map[opening] != c:
            print(False)
            break
        top = -1

else:
    print(top == -1)
            
