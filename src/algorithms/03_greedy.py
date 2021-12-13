
# * Greedy algorithm
# Need maxm / minm

import heapq


def find_minm_cost(arr, size):
    cost = 0
    heapq.heapify(arr)
    while size > 1:
        size -= 1
        min1 = heapq.heappop(arr)
        min2 = heapq.heappop(arr)
        heapq.heappush(arr, min1 + min2)

    return heapq.heappop(arr)


# print(find_minm_cost([2, 3, 5, 7, 9, 13], 6))
# * TC = O(nlogn)
################################################################################


def find_no_of_platforms(arr, dep, size):
    arr = sorted(arr, reverse=False)
    dep = sorted(dep, reverse=False)
    import pdb
    pdb.set_trace()
    plat_needed = 1
    max_platforms = 1
    i, j = 1, 0
    while i < size and j < size:
        pdb.set_trace()
        if arr[i] < dep[j]:
            i += 1
            plat_needed += 1
            if plat_needed > max_platforms:
                max_platforms = plat_needed
        else:
            j += 1
            plat_needed -= 1
    return max_platforms


print(
    find_no_of_platforms(
        [10.00, 10.15, 10.30, 10.40],
        [10.20, 14.00, 15.00, 10.55],
        5))
################################################################################
