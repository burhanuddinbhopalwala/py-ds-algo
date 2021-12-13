import pdb
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
################################################################################


def pow(x: int, n: int):
    if n == 0:
        return 1

    temp = pow(x, n // 2)
    if (n % 2) == 0:
        return temp * temp
    return temp * temp * x


# print(pow(2, 5))
# * TC = O(logn), else O(n) iterative approach
################################################################################

def find_missing_ap(arr: list, start, end, diff):
    if start >= end:
        return float('inf')

    mid = (start + end) // 2
    if arr[mid+1] - arr[mid] != diff:
        return arr[mid] + diff
    elif mid > 0 and arr[mid] - arr[mid-1] != diff:
        return arr[mid-1] + diff

    if arr[mid] == arr[start] + mid * diff:
        return find_missing_ap(arr, mid+1, end, diff)

    return find_missing_ap(arr, start, mid-1, diff)


# print(find_missing_ap([1, 4, 7, 13, 16], 0, 5-1, 3))
# * TC = O(logn)
################################################################################

def search_index(arr, start, end):
    if start >= end:
        return float('inf')

    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        start = mid + 1
    else:
        end = mid - 1
    return search_index(arr, start, end)


# print(search_index([-4, -3, 2, 4, 5], 0, 5-1))
# * TC = O(logn)
################################################################################


def get_peak_element(arr, start, end):
    if start == end:
        return start
    if end == start + 1 and arr[start] >= arr[end]:
        return arr[start]
    elif end == start + 1 and arr[end] >= arr[start]:
        return arr[end]

    mid = (start + end) // 2  # * Hil condiiton
    if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
        return arr[mid]

    if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
        start = mid+1
    else:
        end = mid-1
    return get_peak_element(arr, start, end)


# print(get_peak_element([1, 2, 3, 4, 5, 3], 0, 6-1))
# * TC = O(logn)
################################################################################

def median_2_sorted_arr(arr1, arr2, size):
    if size == 1:
        return (arr1[0] + arr2[0]) / 2
    if size == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2

    median1 = median(arr1, size)
    median2 = median(arr2, size)
    if median1 == median2:
        return median1

    if median2 > median1:
        # Search in right half arr1 and left half of arr2
        # * TODO size % 2 == 0 checks...
        return median_2_sorted_arr(arr1[size//2:], arr2[0:size//2], size // 2)
    # Search in left half arr1 and right half of arr2
    return median_2_sorted_arr(arr1[0:size//2], arr2[size//2:], size // 2)


def median(arr, size):
    """Sorted array."""
    if size % 2 == 0:
        return arr[size // 2]
    else:
        return arr[size//2 - 1] + arr[size//2]


print(median_2_sorted_arr([1, 5, 7, 21, 34], [25, 54, 59, 67, 75], 2))
# * TC = O(logn)
################################################################################


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


# search_sorted_matrix([[1, 2], [3, 4], [10, 60]], 10)
# * TC = O(max(n,m))
################################################################################
