class Solution:
    def checkValidString(self, s: str) -> bool:
        # Index:       0       1        2        3        4          5
        # Character:   (       (        *        )        (          *

        #              1 ────→ 2 ──┬──→ 3 ─────→ 2 ─────→ 3 ──┬──→ 4
        #                          │                          ├──→ 3
        #                          │                          └──→ 2
        #                          │
        #                          ├──→ 2 ─────→ 1 ─────→ 2 ──┬──→ 3
        #                          │                          ├──→ 2
        #                          │                          └──→ 1
        #                          │
        #                          └──→ 1 ─────→ 0 ─────→ 1 ──┬──→ 2
        #                                                     ├──→ 1
        #                                                     └──→ 0 ✓

        # Each node in the graph above tracks the number of opening paranthesis.
        # In traditional validation with no wildcards, you track oppening paranthesis and if the number dips below 0, you have more close
        # than open so you know its wrong. If you end the string and you dont have 0 opening parenthesis, there were opens left unclosed and its wrong
        # if the open number is 0, its all closed and your good.

        # With wildcards, every time you see a star, the openParanthesis tracker splits into three possibilities, +1, -1, and 0
        # notice that at most, the number of open parenthesis can increase by 1 or decrease by 1. Look at index 2, where it split for the first time
        # You get three possibilities, +1, meaning you take * to be open, -1 meaning you take it to be close and 0 meaning you ignore it.
        # Then at index 5, each of these split again. The most important thing to notice that the range of values shifts by at most 1, by the greatest value
        # and the smallest value.
        # If we track two variables, leftmin, the minimum possible number of open parenthesis based on the decisions we made, 
                                    #   leftmax, the maximum possible number of open parenthesis based on the decisions we made,
        # Then each time we encounter a *, when we consider the * to be an open, that means leftmax increases by 1 and when we consider it to be a min, 
            # leftmin decreases by one.
        # With that knowledge, instead of storing all the possible branches, we just store two variables that represent the range of the possible values 
        #  for the number of parenthesis 

        leftmin, leftmax = 0, 0

        for c in s:
            if c == '(':
                leftmin, leftmax = leftmin + 1, leftmax + 1
            elif c == ')':
                leftmin, leftmax = leftmin - 1, leftmax - 1
            else:
                leftmin, leftmax = leftmin - 1, leftmax + 1
            
            # Before, if the number of left parenthesis reached below 0, the whole thing would be 0
            # Here, the only way you know for sure that there is no solution, would be if leftmax dips below 0, because if thats true,
            # Then there is no valid branch. Think about it
            if leftmax < 0:
                return False

            # Its possible for leftmin to dip below 0, but just because leftmin dips below 0, doesnt mean our whole string is invalid. 
            # There could be other values greater than leftmin, greater than 0.
            # However, we dont want to assume that the minimum number of parenthesis is less than 0, that doesnt make sense.
            # so we set it to 0 if that ever happens
            # This also makes sense if you think about it because any branch that dips below 0, we do not want to continue to consider. This prunes them out.
            if leftmin < 0:
                leftmin = 0
            
        return leftmin == 0