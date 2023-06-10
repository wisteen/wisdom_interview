def recursive_search(numbers, target, start=0):
    if start >= len(numbers):
        return False
    
    if numbers[start] == target:
        return True
    
    return recursive_search(numbers, target, start + 1)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Prompt the user to enter a number to search
target = int(input("Enter a number to search: "))

# Call the recursive search function
found = recursive_search(numbers, target)

# Display the result
if found:
    print("Number found in the list!")
else:
    print("Number not found in the list.")