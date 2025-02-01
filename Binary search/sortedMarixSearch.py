
#refer this vidieo for exalainaton https://www.youtube.com/watch?v=VS0BcOiKaGI

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from the top-right corner

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True  # Found target
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False  # Target not found

# Example Usage
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]

target = 9
print(searchMatrix(matrix, target))  # Output: True
