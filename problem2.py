def fibonacci_even_sum(limit):
  a, b = 0, 1
  even_sum = 0
  while b < limit:
    if b % 2 == 0:
      even_sum += b
    a, b = b, a + b
  return even_sum

even_sum = fibonacci_even_sum(4000000)

# Print the sum
print(even_sum)
