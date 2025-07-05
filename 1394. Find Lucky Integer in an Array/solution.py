class Solution(object):
    def findLucky(self, arr):
        hasil = []
        for i in arr:
            if arr.count(i) == i:
                hasil.append(i)
        return max(hasil) if hasil else -1
        