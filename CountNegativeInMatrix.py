"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""
def countneg(grid):
    count = 0
    for i in grid:
        for j in i[::-1]:
            if j<0:
                count+=1
                j+=1
            else:
                break
    return count


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
x = countneg(grid)
print(x)