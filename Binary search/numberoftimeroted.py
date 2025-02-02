def find_rotation_count(arr):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        next_idx = (mid + 1) % len(arr)
        prev_idx = (mid - 1 + len(arr)) % len(arr)

        # Check if mid is the minimum element
        if arr[mid] <= arr[prev_idx] and arr[mid] <= arr[next_idx]:
            return mid  # The number of times the array is rotated

        # If mid element is greater than the last element, search in right half
        elif arr[mid] >= arr[high]:
            low = mid + 1
        else:
            high = mid - 1
    
    return 0  # If the array is not rotated at all

# Example Usage:
arr = [15, 18, 2, 3, 6, 12]
print("Array is rotated:", find_rotation_count(arr), "times")  # Output: 2
