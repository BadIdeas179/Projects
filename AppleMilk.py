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
while len(nums) > 1:
  a = int(input('Apples: '))
  b = int(input('Milks: ')
  main = choice(nums)
  for num in nc:
    if applemilk(main, num, a, m):
      
