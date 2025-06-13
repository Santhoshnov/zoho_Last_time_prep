nums = [5, 5, 4, 6, 4]

map = {}

for num in nums:
    if num in map:
        map[num]+=1
    else:
        map[num]=1

n = len(nums)
for i in range(n):
    for j in range(0,n-i-1):
        a = nums[j]
        b = nums[j+1]

        if map[a]<map[b]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        elif map[a]==map[b]:
            if a>b:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


print(nums)
