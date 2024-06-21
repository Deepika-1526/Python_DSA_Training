def reverse(n, r=0):
  if n == 0:
    return r
  else:
    return reverse(n // 10, r * 10 + n % 10)

def is_palindrome(number, reversed_number):
  return number == reversed_number
number = int(input())
reversed_number = reverse(number)
print(reversed_number)

if is_palindrome(number, reversed_number):
  print("The number is a palindrome.")
else:
  print("The number is not a palindrome.")