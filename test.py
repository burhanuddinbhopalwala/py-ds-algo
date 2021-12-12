# # [0, 1, 1,2,3,5......]

# def fibonacci(n: int) -> list:
#     a = 0
#     b = 1
#     if n == 1:
#         return [a]
#     if n == 2:
#         return [a, b]
#     results = []
#     results.append(a)
#     results.append(b)
#     while n > 2:
#         c = a + b
#         a = b
#         b = c
#         results.append(c)
#         n = n - 1
#     return results


# def fibonacci(n: int) -> list:
#     a = 0
#     b = 1
#     yield a
#     yield b
#     while n > 2:
#         c = a + b
#         a = b
#         b = c
#         yield c
#         n = n - 1
#     return results


# stream = fibonacci(n=10)
# print(next(stream))
# print(next(stream))
# print(next(stream))
# print(next(stream))
# print(next(stream))

# MAX_ASCII = 256
# name = 'Burhanuddin'
# results = {}

# for word in name:
#     if word in results:
#         results[word] += 1
#     else:
#         results[word] = 1

# print(results)

# from collections import Counter
# name = 'Burhanuddin'
# print(Counter(name))
