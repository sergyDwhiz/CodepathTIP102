class Solution(object):
    def satisfiesConditions(self, grid):
        m, n = len(grid), len(grid[0])  # Get the dimensions of the grid

        # Check condition 1: Each cell must be equal to the cell below it (if it exists)
        for i in range(m - 1):  # Iterate through rows except the last row
            for j in range(n):  # Iterate through all columns
                if grid[i][j] != grid[i + 1][j]:
                    return False

        # Check condition 2: Each cell must be different from the cell to its right (if it exists)
        for i in range(m):  # Iterate through all rows
            for j in range(n - 1):  # Iterate through columns except the last column
                if grid[i][j] == grid[i][j + 1]:
                    return False

        return True  # If all checks pass, return True