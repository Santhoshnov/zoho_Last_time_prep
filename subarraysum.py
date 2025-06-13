nums = [1,1,1]
k = 2

#o(n2)
count = 0
for i in range(len(nums)):
    total = 0
    for j in range(i,len(nums)):
        total += nums[j]
        if total == k:
            count+=1

print(count)


#o(n)
nums = [1, 2, 3, -2, 1, 2, -1]
k = 4

count = 0
prefix_sum = 0
prefix_count = {}
prefix_count[0] = 1

for num in nums:
    prefix_sum += num
    sub = prefix_sum - k
    if sub in prefix_count:
        count += prefix_count[sub]
    if prefix_sum in prefix_count:
        prefix_count[prefix_sum] += 1
    else:
        prefix_count[prefix_sum] = 1

print(count)