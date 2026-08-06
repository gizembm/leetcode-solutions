from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count the frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Create buckets
        freq = [[] for _ in range(len(nums) + 1)]

        # Place numbers into their corresponding frequency bucket
        for num, c in count.items():
            freq[c].append(num)

        result = []

        # Traverse buckets from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result