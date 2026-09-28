from random import choice # using random.choice()
def applemilk(main, num, a, m): # main function
  ar = int(main[0] == num[0]) + int(main[1] == num[1]) + int(main[2] == num[2]) + int(main[3] == num[3]) # apples
  al = main.count(num[0]) + main.count(num[1]) + main.count(num[2]) + main.count(num[3]) # all
  return a == ar and m == al - ar # return right / left
# Here will be start and explanations
nums = {str(i) for i in range(1000, 10000)} # all four - digit numbers
nc = nums.copy() # copy nc for nums
for i in nc:
  if sorted(list(i)) != sorted(list(set(list(i)))):
    nums.discard(i) # delete bad numbers
nc = nums.copy() # copy nc for nums
while len(nums) > 1: # main loop
  main = choice(nums) # random
  print(main)
  a = int(input('Apples: ')) # input apples
  b = int(input('Milks: ')) # input milk
  for num in nc:
    if not applemilk(main, num, a, m):
      nums.discard(num) # delete bad numbers
  nc = nums.copy() # copy nc for nums
if nums: # final
  print(f'Your number is{nums[0]}.')
else:
  print('There isn\'t any')
