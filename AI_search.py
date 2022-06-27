 #%% STACK CLASS

# Combined all search algorithms and required data structures

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self):        
    return self.stack.pop()

  def empty(self):
    return len(self.stack) == 0

#%% QUEUE CLASS

from collections import deque
class Queue:
  def __init__(self):
    self.queue = deque()
	  
  def push(self, item):
    self.queue.append(item)
	  
  def pop(self):
    return self.queue.popleft()
	  
  def empty(self):
    return len(self.queue) == 0

#%% PRIORITY QUEUE CLASS

import heapq

class PriorityQueue:
  def __init__(self, priorityFunction):
      self.priorityFunction = priorityFunction
      self.heap = []
      
  def push(self, item):
      heapq.heappush(self.heap, (self.priorityFunction(item), item))
      
  def pop(self):
      (_, item) = heapq.heappop(self.heap)
      return item
      
  def empty(self):
      return len(self.heap) == 0

#%% SEARCHING ALGORITHMS

def generalSearch(problem, strategy):
    strategy.push(problem.getStartState())
    #! Added counters to keep track of number of nodes expanded / generated  
    num_nodes_exp = 0
    num_nodes_gen = 1
    while not strategy.empty():
        num_nodes_exp += 1

        #! uncomment to print priority queue at each stage
        #! print(strategy.heap)
        node = strategy.pop()

        # uncomment to print node being expanded
        print(node)
        if problem.isGoalState(node):
            return (node, num_nodes_exp, num_nodes_gen) #! Return the final state along with num nodes exp/gen
        for move in problem.getSuccessors(node):            
            strategy.push(move)
            num_nodes_gen += 1
        # uncomment to print num of nodes generated after each node expansion
        # print(num_nodes_gen)
    return None

def depthFirstSearch(problem):
    return generalSearch(problem, Stack())

def breadthFirstSearch(problem):
    return generalSearch(problem, Queue())

#%% IDA


def iterativeDeepeningSearch(problem):
  num_nodes_exp = 0
  num_nodes_gen = 1
  #! moved depthLimitedDFS inside and made counters as above
  def depthLimitedDFS(problem, state, depth):
      nonlocal num_nodes_gen, num_nodes_exp
      num_nodes_exp+=1
      if problem.isGoalState(state):
          return state
      if depth <= 0:
          return None
      for move in problem.getSuccessors(state):
          num_nodes_gen += 1
          solution = depthLimitedDFS(problem, move, depth-1)
          if solution is not None:
              return solution
      return None

  depth = 1
  while True:
    solution = depthLimitedDFS(problem, problem.getStartState(), depth)
    if solution is not None:
      return (solution, num_nodes_exp, num_nodes_gen)
    depth += 1 
       
#%%
def uniformCostSearch(problem):
    return generalSearch(problem, PriorityQueue(lambda state: (sum(state[3]) if len(state) > 3 else len(state[-1]))))
    
def greedySearch(problem, heuristic):
    return generalSearch(problem, PriorityQueue(heuristic))
    
def astarSearch(problem, heuristic):
    #! the given function simple took length of steps to curr state as current cost (ie assuming uniformcost)
    #! also, number of elements in state is diff for diff problems. hence the following checks are req
    totalCost = lambda state: (sum(state[3]) if len(state) > 3 else len(state[2])) + heuristic(state)
    return generalSearch(problem, PriorityQueue(totalCost))

    

# Ashith Farhan 79866
# Joel DSouza 79296
# Farooq Mirza 80205
# Sabbir Alam 79438
