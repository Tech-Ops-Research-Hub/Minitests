def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Example 
numbers = [12, 45, 7, 89, 34]
print("Largest number is:", find_largest(numbers))