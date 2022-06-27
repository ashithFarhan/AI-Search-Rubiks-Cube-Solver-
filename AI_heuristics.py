#HAMMING DISTANCE
from heapq import heappop
 
# these are designed for 8-puzzle problem
# variations of these functions for other problems are defined within the problem class

class AI_heuristics: #! moved it into a class
  def hammingDistance(grid):
      #! State passed is a tuple of the form (grid, pos0, path) 
      grid = grid[0] #! hence this is required
      hd = len([i for i in range(len(grid)) if grid[i] != 0 and grid[i] != i+1])
      return hd

  # print(hammingDistance(([2,1,3,4,5,6,7,8,0], 8, [])))

  #MANHATTAN DISTANCE
  def manhattanDistance(grid):
      grid = grid[0]
      def distance(i):
          return 0 if grid[i] == 0 else abs(((grid[i]-1) / 3) - (i / 3)) + abs(((grid[i]-1) % 3) - (i % 3))
      return sum(distance(i) for i in range(len(grid)))



# Ashith Farhan 79866
# Joel DSouza 79296
# Farooq Mirza 80205
# Sabbir Alam 79438
