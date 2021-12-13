import math

# * TC = O(logn) - Binary search first occurrence and last occurrence


def binary_search(arr: list, ele: int, start, end, first_occ=True):
    result = -1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == ele:
            result = mid
            if first_occ:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    return result


arr = [1, 2, 3, 4, 5, 5, 5, 7, 8, 9]
# print(binary_search(arr, 5, 0, len(arr) - 1, first_occ=False))
# * TC = O(logn) - Binary search first occurrence and last occurrence


def pow(x: int, n: int):
    if n == 0:
        return 1

    temp = pow(x, n//2)
    if n % 2:
        return temp * temp
    return temp * temp * x


# print(pow(2, 5))

def search_sorted_matrix(mat: [[]], ele: int):
    row = len(mat)
    col = len(mat[0])

    i = 0
    j = col-1
    while i < row and j > -1:
        if mat[i][j] == ele:
            print(f'Found in>>>>: {i}, {j}')
            return
        elif mat[i][j] > ele:
            j -= 1
        else:
            i += 1
    print('Not found')


search_sorted_matrix([[1, 2], [3, 4], [10, 60]], 10)
