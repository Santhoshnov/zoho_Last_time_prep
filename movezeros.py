nums = [0,1,0,3,12]

# extra space
split1 = []
split2 = []

for num in nums:
    if num == 0:
        split2 += [num]
    else:
        split1 += [num]
print(split1+split2)


# without extra space

i=0
j=1
while i<len(nums) and j<len(nums):
    if nums[i] == 0 and nums[j] !=0:
        nums[i], nums[j] = nums[j], nums[i]
        i+=1
        j+=1
    elif nums[i] == 0 and nums[j] == 0:
        j+=1
    else:
        i+=1
        if j<=i:
            j=i+1

print(nums)
