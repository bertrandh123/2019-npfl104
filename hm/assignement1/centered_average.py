def centered_average(nums):
  nums.sort()
  if len(nums)%2==1:
    return nums[len(nums)//2]
  else:
    return (nums[len(nums)//2 - 1]+nums[len(nums)//2])/2


print('centered_average([1, 2, 3, 4, 100]) == 3 -> '+str(centered_average([1, 2, 3, 4, 100]) == 3))
