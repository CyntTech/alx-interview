 #!/usr/bin/python3
  2 """Perimeter of an Island"""
  3
  4
  5 def island_perimeter(grid):
  6     """
  7     A function that determines the perimeter of an island de    scribed in a list of integers.
  8     """
  9     perimeter = 0
 10     for i in range(len(grid)):
 11         for j in range(len(grid[i])):
 12             if grid[i][j] == 1:
 13                 perimeter += 4
 14                 if (i > 0 and grid[i - 1][j] == 1):
 15                     perimeter -= 2
 16                 if (j > 0 and grid[i][j - 1] == 1):
 17                     perimeter -= 2
 18     return perimeter
