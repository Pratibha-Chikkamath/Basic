def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def second_largest_prime(arr):
    count = 0
    primes = []

    # Start from the end (since array is sorted in ascending order)
    for i in range(len(arr) - 1, -1, -1):
        if is_prime(arr[i]):
            primes.append(arr[i])
            count += 1
            if count == 2:
                return arr[i]

    return None  # Not enough primes

# Example
arr = [1, 4, 6, 7, 9, 11, 13, 15, 17]
print(second_largest_prime(arr))  # Output: 13
