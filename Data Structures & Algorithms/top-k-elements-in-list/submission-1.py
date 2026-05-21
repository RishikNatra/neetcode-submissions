class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        arr = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for num, cnt in freq.items():
            arr[cnt].append(num)
        res=[]
        for j in range(len(arr) - 1, 0, -1):
            for num in arr[j]:
                res.append(num)
                if len(res) == k:
                    return res