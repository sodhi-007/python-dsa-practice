"""
LeetCode 977: Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array
of the squares of each number, also sorted in non-decreasing order.

Approach: two pointers
- The largest square is always at one of the two ends (negatives can be big).
- Compare the ends, take the larger square, move that pointer inward.
- This builds the result from largest to smallest, so reverse it at the end.

Time:  O(n)
Space: O(n) for the output list
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums) - 1
        result = []

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l] ** 2)
                l += 1
            else:
                result.append(nums[r] ** 2)
                r -= 1

        # .reverse() works in place and returns None,
        # so reverse first, then return the list itself.
        result.reverse()
        return result


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([1, 2, 3], [1, 4, 9]),
        ([-3, -2, -1], [1, 4, 9]),
        ([0], [0]),
        ([-5], [25]),
    ]

    for nums, expected in test_cases:
        output = sol.sortedSquares(nums)
        status = "PASS" if output == expected else "FAIL"
        print(f"{status}  input={nums}  output={output}  expected={expected}")
