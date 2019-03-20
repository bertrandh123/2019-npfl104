def big_diff(nums):
  l=[]
  for i in range(len(nums)):
    for j in range(i,len(nums)):
      l.append(abs(nums[i]-nums[j]))
  return max(l)



print('big_diff([10, 3, 5, 6]) ==7 -> '+str(big_diff([10, 3, 5, 6]) ==7))
