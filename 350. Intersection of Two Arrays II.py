from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        count2 = {}
        
        # Hitung frekuensi elemen dalam nums1
        for num in nums1:
            if num in count1:
                count1[num] += 1
            else:
                count1[num] = 1
        print(f"count1: {count1}")
        
        # Hitung frekuensi elemen dalam nums2
        for num in nums2:
            if num in count2:
                count2[num] += 1
            else:
                count2[num] = 1
        print(f"count2: {count2}")
        
        result = []
        
        # Tentukan elemen yang muncul di kedua array
        for num in count1:
            if num in count2:
                min_count = min(count1[num], count2[num])
                print(f"num: {num}, count1[num]: {count1[num]}, count2[num]: {count2[num]}, min_count: {min_count}")
                result.extend([num] * min_count)
        
        print(f"result: {result}")
        return result

# Test dengan contoh
sol = Solution()
print(sol.intersect([5, 2, 2, 5], [2, 2]))  # Output: [2, 2]