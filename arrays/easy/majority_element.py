class MajorityElement:
    """
    Time Complexity : O(N)
    Space Complexity : O(1)
    """

    def find_majority_element(self, nums: list):
        majority_element = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if counter <= 0:
                majority_element = nums[i]
            if nums[i] == majority_element:
                counter += 1
            else:
                counter -= 1
        return majority_element


if __name__ == '__main__':
    majority_element = MajorityElement()
    print(majority_element.find_majority_element([4, 4, 2, 3, 4]))
