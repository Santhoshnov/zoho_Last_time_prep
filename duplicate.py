nums = [1,3,4,2,2]

#o(n2)
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            print(nums[i])

#o(n)
map = {}

for num in nums:
    if num in map:
        print(num)
    else:
        map[num] = 1

        