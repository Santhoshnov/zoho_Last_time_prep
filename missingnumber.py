nums = [9,6,4,2,3,5,7,0,1]

n_sum = 0
actual_sum = 0

for num in nums:
    actual_sum += num

for i in range(len(nums)+1):
    n_sum += i

print(n_sum-actual_sum)