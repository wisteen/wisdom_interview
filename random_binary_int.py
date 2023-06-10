import random

# Generate a random 4-digit number consisting of 0s and 1s
# binary_num = ''
# for _ in range(4):
#     binary_num += random.choice(['0', '1'])

# let me reduce it a bit
binary_num = ''.join(random.choice(['0', '1']) for _ in range(4))



# Convert the binary number to base 10
decimal_num = int(binary_num, 2)

# Print the generated binary number and its base 10 equivalent
print("Generated Binary Number:", binary_num)
print("Decimal Equivalent:", decimal_num)
