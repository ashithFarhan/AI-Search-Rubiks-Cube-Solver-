# AI-Search-Rubiks-Cube-Solver

- An AI search implementation including common algorithms like A*, BFS, DFS, UCS, IDS, etc. for comparing performances  
- The hamming distance heuristic was used for the A* and greedy search algorithms
- Complete problem formulation for a 3x3x3 Rubik's cube, represented as a 3D matrix of sub-cubes.  
- Moves are represented using [common notations](https://ruwix.com/the-rubiks-cube/notation/)
<br>

![rubikscubefigure](https://user-images.githubusercontent.com/70636393/176030449-82d30664-f3f2-478a-8d6a-54d7f8cc7042.png)

## Results

- A* search with only hamming distance as heuristic showed massive improvement in time/space complexity in finding the solution, compared to the others, especially breadth first search, which required almost 250 times as many nodes to be generated
- Depth first search did not work due to the infinite search tree, but IDS did, when it reached depth 3 and showed much better performance than BFS
- Greedy search did not resolve and started moving down an infinite cyclic path (as confirmed by printing intermediate states) as it is only guided by heuristics
