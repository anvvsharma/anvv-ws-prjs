
def calculate_average(num):
    total = sum(num)
    count = len(num)
    average = total / count

    return average

# Test the function
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("average numbers are :", average)
