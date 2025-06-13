nums = [2,7,11,15]
target = 9

#o(n2)
for i in range(len(nums)):
    for j in range(1,len(nums)):
        if nums[i]+nums[j] == target:
            print([i,j])

#o(n)
map = {}
for i in range(len(nums)):
    sub = target - nums[i]
    if sub in map:
        print([map[sub],i])
        break
    map[nums[i]] = i

