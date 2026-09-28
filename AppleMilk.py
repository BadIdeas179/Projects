from random import choice # using random.choice()
def applemilk(main, num, a, m): # main function
  return True
# Here will be start and explanations
nums = {str(i) for i in range(1000, 10000)} # all four - digit numbers
nc = nums.copy() # copy nc for nums
for i in nc:
  if sorted(list(i)) != sorted(list(set(list(i)))):
    nums.discard(i) # delete bad numbers
nc = nums.copy() # copy nc for nums
while len(nums) > 1: # main loop
  a = int(input('Apples: ')) # input apples
  b = int(input('Milks: ') # input milk
  main = choice(nums) # random
  for num in nc:
    if not applemilk(main, num, a, m):
      nums.discard(num) # delete bad numbers
  nc = nums.copy() # copy nc for nums
if nums: # final
  print(f'Your number is{nums[0]}.')
else:
  print('There isn\'t any')
