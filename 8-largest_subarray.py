def maximumSubarraySum(numbers):

max_sum,begin,end = 0, 0 , 0
  for i in range(len(numbers)):
      current_sum=0
  for j in range(i,len(numbers)):
      current_sum+=numbers[j]
  if max_sum<current_sum:
      max_sum=current_sum
      begin,end=i,j
      print("largest sum is ",max_sum)
      print("largest sum contiguous subarray: ",end="")
  for i in range(begin,end+1):
      print(numbers[i],end='\t')
      numbers = [-10,5,1,6,-9,2,-7,3,-5]
      maximumSubarraySum(numbers)