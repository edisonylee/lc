class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to set for O(1) average-time lookups
        # This also removes duplicates, which don't affect consecutive sequences
        num_set = set(nums)

        # Tracks the length of the longest consecutive sequence found
        longest = 0

        # Iterate through each unique number
        for n in num_set:
            # Only start counting if `n` is the BEGINNING of a sequence
            # (i.e., there is no number immediately before it)
            if n - 1 not in num_set:
                length = 0  # Length of the current consecutive sequence

                # Count forward while consecutive numbers exist
                while n + length in num_set:
                    length += 1

                # Update global maximum if this sequence is longer
                longest = max(longest, length)

        # Return the length of the longest consecutive sequence
        return longest
