'''def add_numbers(numbers):
    int_sum = 0
    float_sum = 0.0
    
    for number in numbers:
        if isinstance(number, int):
            int_sum += number
        elif isinstance(number, float):
            float_sum += number
    
    return int_sum, float_sum

numbers = [1, 2.5, 3, 4.75, 5]
int_sum, float_sum = add_numbers(numbers)
print(f"Sum of integers: {int_sum}")
print(f"Sum of floats: {float_sum}")'''
input_string = "5 ,3.8, 7, 5.6 ,4 ,2 ,3"

# Split the input string by commas and convert elements to numbers
numbers = [float(x.strip()) for x in input_string.split(',')]

# Initialize sums
sum_even = 0
sum_odd = 0
sum_decimal = 0

# Iterate through the numbers and update sums accordingly
for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
    
    if num != int(num):
        sum_decimal += num

# Print the sums
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
print("Sum of decimal numbers:", sum_decimal)
