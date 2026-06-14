class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        curr_sum = 0
        max_sum = 0

        # First window
        for i in range(k):
            curr_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        if len(freq) == k:
            max_sum = curr_sum

        left = 0

        for right in range(k, len(nums)):
            # Remove left element
            curr_sum -= nums[left]
            freq[nums[left]] -= 1

            if freq[nums[left]] == 0:
                del freq[nums[left]]

            left += 1

            # Add right element
            curr_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # Valid window?
            if len(freq) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum