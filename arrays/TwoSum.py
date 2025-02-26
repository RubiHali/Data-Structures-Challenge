class TwoSum:
    """
    Time complexity : O(N)
    Space Complexity : O(N)
    Using Dictionary / Hash Map for solving this array problem
    """
    def find_pair(self, nums: list, target: int) -> list:
        sum_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in sum_map:
                return [sum_map.get(diff), i]
            sum_map[n] = i
        return [-1, -1]


if __name__ == '__main__':
    two_sum = TwoSum()
    print(two_sum.find_pair([3, 4, 5, 6], 11))
