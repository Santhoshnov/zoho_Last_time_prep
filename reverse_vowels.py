s = "IceCreAm"

vowels = "aeiouAEIOU"

seen = set(vowels)

s_list = list(s)

i = 0
j = len(s_list)-1

while i < j:
    if s_list[i] in seen and s_list[j] in seen:
        s_list[i],s_list[j] = s_list[j],s_list[i]
        i+=1
        j-=1
    elif s_list[i] in seen:
        j-=1
    else:
        i+=1

s=''.join(s_list)
print(s)
    
