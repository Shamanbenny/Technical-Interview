class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # If something is repeatable within itself, then it is repeatable within double of itself.
        doubled = s + s
        return s in doubled[1:-1]
        # Check with offset to prevent `True` because doubled contains s in its first or second half
        #   That is, we check if s is within the middle segment of doubled
