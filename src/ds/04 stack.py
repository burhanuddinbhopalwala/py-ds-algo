intervals = [
    (3, 4),
    (7, 9),
    (1, 5),
    (2, 9),
    (4, 5),
    (33, 55),
    (22, 50),
    (2, 33), (77, 99)]


def merge_overlap(intervals: list(tuple())):
    intervals = sorted(intervals, key=lambda x: x[0], reverse=True)

    stack, results = [], []
    for interval in intervals:
        stack.append(interval)

    results.append(stack.pop())
    # * bool(non-empty): True
    while bool(stack):
        interval = stack.pop()
        last_interval = results[-1]
        if interval[0] > last_interval[1]:
            # Non Overlapping case
            results.append(interval)
        else:
            results.pop()
            start = min(interval[0], last_interval[0])
            end = max(interval[1], last_interval[1])
            results.append((start, end))

    return results


# * TC = O(nlogn) Includes sorting
# print(merge_overlap(intervals))


def closest_greater_right(nums: list) -> list:
    stack = []
    stack.append(0)
    results = [float('-inf')] * len(nums)

    for index, element in enumerate(nums[1:]):
        while bool(stack) and element > nums[stack[-1]]:
            results[stack[-1]] = element
            stack.pop()
        stack.append(index)

    return results

# * TC = O(n)
# print(closest_greater_right([6, 3, 4, 9, 2, 1]))


# * Stock Span problem
def evaluate_span(nums: list):
    stack = []
    results = [0] * len(nums)

    stack.append(0)
    results.append(0)

    for index, element in enumerate(nums[1:]):
        span = 0
        while bool(stack) and element > nums[stack[-1]]:
            span += 1
            stack.pop()
        results[index] = span if span > 0 else 0
        stack.append(index)
    return results

# * TC = O(n)
# print(evaluate_span([6, 3, 4, 9, 2, 1]))

# * Get minimum in O(1)


class Stack(object):
    def __init__(self):
        self.top = -1
        self.store = []
        self.minm = float("inf")

    def push(self, ele: int):
        if ele < self.minm:
            self.store.append(ele - self.minm)
            self.minm = ele
        else:
            self.store.append(ele)
        self.top += 1

    def pop(self):
        if self.top == -1:
            return self.minm
        self.top -= 1
        temp = self.store.pop()
        if self.minm > temp:
            temp = self.minm
            self.minm = self.minm - temp
        return temp

    def find_minimum(self):
        # * O(1)
        return self.minm


# s = Stack()
# s.push(4)
# s.push(3)
# print(s.find_minimum())  # * 3
# print(s.pop())  # * 3
# print(s.find_minimum())  # * 4

def reverse_string_stack(string: str):
    stack = []
    results = []
    for char in string:
        stack.append(char)

    while bool(stack):
        results.append(stack.pop())
    return ''.join(results)


# print(reverse_string_stack("Burhanuddin"))
