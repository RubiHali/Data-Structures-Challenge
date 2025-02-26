class MoveZeroes:
    """
    Time Complexity : O(N)
    Space Complexity : O(1)
    """

    def move_zeroes(self, nums: list):
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0 and right > 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums


if __name__ == '__main__':
    num_zeroes = MoveZeroes()
    print(num_zeroes.move_zeroes([0, 1, 0, 3, 12, 0]))
