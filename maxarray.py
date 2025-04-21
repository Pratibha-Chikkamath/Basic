user_input = input("Enter your array (space-separated): ")
my_array = [int(x) for x in user_input.split()]
def find_max(arr):
    if not arr:
        return None  # or raise an error if array is empty

    max_val = arr[0]  # assume the first element is the max
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Example usage:
#my_array = [3, 7, 2, 9, 4]
print("Maximum value:", find_max(my_array))
