def divisible_by_ten(nums):
  divisible = []
  for num in nums:
    if num % 10 == 0:
      divisible.append(num)
  return divisible

def evenly_divisible(nums, divisor):
  return [i for i in nums if i % divisor == 0]

numbers = [20, 25, 30, 35, 40]
print(numbers)
print(divisible_by_ten(numbers))
print(evenly_divisible(numbers, 10))
