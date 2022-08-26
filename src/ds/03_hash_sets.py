
# * Duplicates within k


def check_duplicates_k(nums, k):
    s = set()
    for index, num in enumerate(nums):
        if num in s:
            print(f'Duplicate in k distance: {num}')
        if index > k:
            s.discard(nums[index - k])
        s.add(num)
    s.clear()
################################################################################


def distinct_k_window(nums, k):
    s = set()
    result = 0

    for index, ele in enumerate(nums[:k]):
        if ele in s:
            result -= 1
            continue
        s.add(ele)
        result += 1
    for index in range(k, len(nums)):
        result += k
        s.discard(nums[index-k])
        if nums[index] in s:
            result -= 1
        s.add(nums[index])
    return result
################################################################################


def disjoint_set(nums1, nums2):
    s1 = set()
    for num in nums1:
        s1.add(num)
    for num in nums2:
        if num in s1:
            return False
    return True
################################################################################


def group_by_first_occ(nums):
    h = {}
    # * h = Counter(nums)
    for num in nums:
        if num in h:
            h[num] += 1
        else:
            h[num] = 1
    for index, num in enumerate(nums):
        try:
            counter = h[num]
            while counter > 0:
                print(num)
                counter -= 1
            del h[num]
        except KeyError as key_error:
            continue


nums = [2, 3, 5, 6, 8, 5, 8, 9, 9]
# check_duplicates_k(nums, 2)
# print(disjoint_set(nums, [20, 80, 90]))
# print(group_by_first_occ(nums))
nums = [2, 3, 5, 6]
print(distinct_k_window(nums, 3))
################################################################################
