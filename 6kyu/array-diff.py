# Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.
# Examples
#
# If a = [1, 2] and b = [1], the result should be [2].
#
# If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
from certifi import where


def array_diff(a, b):
    diff = list(filter(lambda x: x not in b, a))

    return diff

print(array_diff([1, 2, 2, 2, 3], [2]))