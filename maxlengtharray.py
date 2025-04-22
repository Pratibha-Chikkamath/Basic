# Get input from user and convert it to a list of integers
user_input = input("Enter your array (space-separated): ")
my_array = [int(x) for x in user_input.split()]

# Function to find length of the array
def find_length(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

# Print the length
print("Length of array:", find_length(my_array))
