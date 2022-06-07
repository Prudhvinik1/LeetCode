class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        main_ptr = m + n -1
        nums1_ptr = m - 1
        nums2_ptr = n - 1
        
        while nums1_ptr >=0 and nums2_ptr >= 0:
            if(nums1[nums1_ptr] < nums2[nums2_ptr]):
                nums1[main_ptr] = nums2[nums2_ptr]
                nums2_ptr -= 1
                main_ptr -= 1
                
            elif(nums1[nums1_ptr] >= nums2[nums2_ptr]):
                nums1[main_ptr] = nums1[nums1_ptr]
                nums1_ptr -= 1
                main_ptr -= 1
            
        
        while nums1_ptr >= 0:
            nums1[main_ptr] = nums1[nums1_ptr]
            main_ptr -= 1
            nums1_ptr -= 1
        
        while nums2_ptr >= 0:
            nums1[main_ptr] = nums2[nums2_ptr]
            main_ptr -= 1
            nums2_ptr -= 1
            