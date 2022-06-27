from AI_search import *
from EightPuzzleProblem import *
from PacmanProblem import *
from StonePuzzleProblem import *
from TravellingSalesmanProblem import *
from RiverCrossingProblem import *
from RubiksCubeProblem import *

def solve(problem, *algs):

    def print_info(solution): # Function to print info from returned solution
          if not solution:
            print("No solution!")
            return
          state, num_nodes_exp, num_nodes_gen = solution
          if isinstance(problem, EightPuzzleProblem)or isinstance(problem, StonePuzzleProblem) or isinstance(problem, RiverCrossingPuzzleProblem) or isinstance(problem, RubiksCubeProblem):
            finalstate,_,steps = state
            cost = len(steps)
          elif isinstance(problem, TravellingSalesmanProblem):
            finalstate,_,steps, cost = state
            cost = sum(cost)
          else:
            finalstate, steps = state
            cost = len(steps)
          print(f"Final state: {finalstate}")
          print(f"Solution: {steps}")
          print(f"Cost: {cost}")
          print(f"Number of nodes expanded: {num_nodes_exp}")
          print(f"Number of nodes generated: {num_nodes_gen}")
          print("="*80+"\n")


    print(problem.__class__.__name__)
    
    for alg in algs:
        
        if alg.__name__ in ["greedySearch", "astarSearch"]: # check if function needs heuristic
            for heuristic in problem.getHeurisitcs():
              print(f"Algorithm used: {alg.__name__}")
              print(f"Heuristic used: {heuristic.__name__}")
              solution = alg(problem, heuristic)
              print_info(solution)

        else:
            print(f"Algorithm used: {alg.__name__}")
            solution = alg(problem)
            print_info(solution)


solve(EightPuzzleProblem([4,1,3,0,2,5,7,8,6]), breadthFirstSearch, uniformCostSearch, greedySearch, astarSearch) # DFS and IDS will not find a solution

solve(PacmanProblem(["P--",
                     "-%-",
                     "-.-"], (0,0), (2,1)), breadthFirstSearch,  greedySearch, astarSearch)


solve(StonePuzzleProblem(), breadthFirstSearch, depthFirstSearch, uniformCostSearch, greedySearch, astarSearch, iterativeDeepeningSearch)

solve(RiverCrossingPuzzleProblem(), breadthFirstSearch, uniformCostSearch, greedySearch, astarSearch, iterativeDeepeningSearch)

solve(TravellingSalesmanProblem([[0,20,42,35],
                                 [20,0,30,34],
                                 [42,30,0,12],
                                 [35,34,12,0]], 1), breadthFirstSearch, depthFirstSearch, uniformCostSearch, greedySearch, astarSearch, iterativeDeepeningSearch)

# Ashith Farhan 79866
# Joel DSouza 79296
# Farooq Mirza 80205
# Sabbir Alam 79438
