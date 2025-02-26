class MergeArrays:

    """
    Time Complexity : O(N)
    Space Complexity : O(1)
    """
    def merge(self, nums1: list, nums2: list, m: int, n: int):
        k = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[k] = nums1[p1]
                p1 -= 1
            else:
                nums1[k] = nums2[p2]
                p2 -= 1
            k -= 1
        while p2 >= 0:
            nums1[k] = nums2[p2]
            p2 -= 1
            k -= 1
        return nums1


if __name__ == "__main__":
    merge_arrays = MergeArrays()
    print(merge_arrays.merge([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3))
