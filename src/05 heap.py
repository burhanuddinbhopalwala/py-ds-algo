import heapq


class Heap(object):
    def __init__(self, nums: list):
        self.store = nums
        self.build_min_heap()

    def min_heapify(self, nums: list, size: int, index):
        left: int = 2*index + 1
        right: int = 2*index + 2
        smallest: int = index

        if size > left and self.store[smallest] > self.store[left]:
            smallest = left

        if size > right and self.store[smallest] > self.store[right]:
            smallest = right

        if smallest != index:
            temp = self.store[index]
            self.store[index] = self.store[smallest]
            self.store[smallest] = temp
            self.min_heapify(self.store, size, smallest)

    def build_min_heap(self):
        for index in range(0, len(self.store) // 2):
            self.min_heapify(self.store, len(self.store), index)

    def pop(self):
        pop = self.store.pop(0)
        self.min_heapify(self.store, len(self.store), 0)
        return pop


heap = Heap([10, 20, 3, 4, 5, 6, 7])
print(heap.pop())
print(heap.pop())
print(heap.pop())


# class Solution(object):
#     @staticmethod
#     def findKthLargest(nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         heapq.heapify(nums)
#         for i in range(len(nums) - k):
#             heapq.heappop(nums)
#         return heapq.heappop(nums)


# print(Solution.findKthLargest([1, 2, 3, 4, 5, 6, 7], 3))
