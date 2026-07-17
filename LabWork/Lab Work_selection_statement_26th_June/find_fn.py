# Function to find maximum number
def find_max(numbers):
    return max(numbers)

# Function to find minimum number
def find_min(numbers):
    return min(numbers)

# Function to find average
def find_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average


# Main Program
numbers = []

print("Enter 10 integers:")
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

print("\nList =", numbers)
print("Maximum value =", maximum)
print("Minimum value =", minimum)
print("Average =", average)