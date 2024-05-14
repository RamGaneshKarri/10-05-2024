minimum = float('inf')

# Input 10 numbers from the user

for i in range(10):
    num = int(input())
    # Update the minimum number if the current number is smaller
    if num < minimum:
        minimum = num

# Output the minimum number
print("Thank you! {} is the smallest number.".format(minimum))
