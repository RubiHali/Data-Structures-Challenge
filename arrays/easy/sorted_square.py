class SortedSquare:
    """
    Time Complexity : O(N)
    Space Complexity : O(N)
    """
    def sorted_square(self, nums: list):
        output = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        k = len(nums) - 1
        while left <= right:
            left_num = abs(nums[left])
            right_num = abs(nums[right])
            if left_num >= right_num:
                output[k] = left_num ** 2
                left += 1
            else:
                output[k] = right_num ** 2
                right -= 1
            k -= 1
        return output


if __name__ == "__main__":
    sorted_square = SortedSquare()
    print(sorted_square.sorted_square([-4, -1, 3, 6, 10]))
