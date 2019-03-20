def count_evens(nums):
  S=0
  for i in range(len(nums)):
    if nums[i]%2==0:
      S+=1
  return S

print('count_evens([2, 1, 2, 3, 4]) ==3 -> '+str(count_evens([2, 1, 2, 3, 4]) ==3))
