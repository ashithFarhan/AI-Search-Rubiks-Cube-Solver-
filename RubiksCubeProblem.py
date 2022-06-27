import copy
from AI_problem import SearchProblem

class RubiksCubeProblem(SearchProblem):
    
    # grid is nxn matrix of distances from each city to the other.
    # pos0 is the salesman position.
    # travelled is the list of cities already travelled to.
    def __init__(self, cube):
        self.cube = cube

    def getStartState(self):
        return (self.cube, 0, [])

    def isGoalState(self, state):
        return state[0].grid.__str__() == "[[[[('y', 'W'), ('z', 'R'), ('xi', 'G')], [('y', 'W'), ('z', 'R')], [('x', 'B'), ('y', 'W'), ('z', 'R')]], [[('y', 'W'), ('xi', 'G')], [('y', 'W')], [('x', 'B'), ('y', 'W')]], [[('y', 'W'), ('xi', 'G'), ('zi', 'O')], [('y', 'W'), ('zi', 'O')], [('x', 'B'), ('y', 'W'), ('zi', 'O')]]], [[[('z', 'R'), ('xi', 'G')], [('z', 'R')], [('x', 'B'), ('z', 'R')]], [[('xi', 'G')], [], [('x', 'B')]], [[('xi', 'G'), ('zi', 'O')], [('zi', 'O')], [('x', 'B'), ('zi', 'O')]]], [[[('z', 'R'), ('xi', 'G'), ('yi', 'Y')], [('z', 'R'), ('yi', 'Y')], [('x', 'B'), ('z', 'R'), ('yi', 'Y')]], [[('xi', 'G'), ('yi', 'Y')], [('yi', 'Y')], [('x', 'B'), ('yi', 'Y')]], [[('xi', 'G'), ('yi', 'Y'), ('zi', 'O')], [('yi', 'Y'), ('zi', 'O')], [('x', 'B'), ('yi', 'Y'), ('zi', 'O')]]]]"

    def getSuccessors(self, state):
        moves = []
        cube, _, path = state

        def generateMove(move, action):
            pathCopy = list(path)
            pathCopy.append(action)
            cubeCopy = list(cube)
            cubeCopy.move()
            moves.append((cubeCopy, 0, pathCopy))

        for move in dir(Cube):
            if not move.startswith("__"):
                generateMove(move, move.__name__)
        
        # uncomment to see generated nodes
        # print([i[2] for i in moves])
        return moves

    def getHeurisitcs(self):
        def hammingDistance(grid):
          grid = grid[-1]
          return grid[-1]
        return [hammingDistance]

class Block:
    def __init__(self, x='-', y='-', z='-', xi='-', yi='-', zi='-'):
        self.colors = {'x': x, 'y': y, 'z': z, 'xi': xi, 'yi':yi, 'zi': zi}
        self.position = (-1,-1,-1)
        # self.orientation = ('x', 'y', 'z')
    
    def __repr__(self):
        x=[(k,v)  for k,v in self.colors.items() if v!='-']
        return f"{x}"

    def F(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['x'] = self.colors['y'] 
        newc['y'] = self.colors['xi']
        newc['yi'] = self.colors['x']
        newc['xi'] = self.colors['yi']
        newc['z'] = self.colors['z']
        self.colors = newc
    
    def U(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['xi'] = self.colors['z'] 
        newc['zi'] = self.colors['xi']
        newc['z'] = self.colors['x']
        newc['x'] = self.colors['zi']
        newc['y'] = self.colors['y']
        self.colors = newc
    
    def R(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['y'] = self.colors['z'] 
        newc['zi'] = self.colors['y']
        newc['yi'] = self.colors['zi']
        newc['z'] = self.colors['yi']
        newc['x'] = self.colors['x']
        self.colors = newc
    
    def L(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['z'] = self.colors['y'] 
        newc['yi'] = self.colors['z']
        newc['zi'] = self.colors['yi']
        newc['y'] = self.colors['zi']
        newc['xi'] = self.colors['xi']
        self.colors = newc
    
    def D(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['x'] = self.colors['z'] 
        newc['zi'] = self.colors['x']
        newc['xi'] = self.colors['zi']
        newc['z'] = self.colors['xi']
        newc['yi'] = self.colors['yi']
        self.colors = newc

    def B(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['y'] = self.colors['x'] 
        newc['xi'] = self.colors['y']
        newc['yi'] = self.colors['xi']
        newc['x'] = self.colors['yi']
        newc['zi'] = self.colors['zi']
        self.colors = newc
    
    def Fi(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['y'] = self.colors['x'] 
        newc['xi'] = self.colors['y']
        newc['yi'] = self.colors['xi']
        newc['x'] = self.colors['yi']
        newc['z'] = self.colors['z']
        self.colors = newc
    
    def Ui(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['x'] = self.colors['z'] 
        newc['zi'] = self.colors['x']
        newc['xi'] = self.colors['zi']
        newc['z'] = self.colors['xi']
        newc['y'] = self.colors['y']
        self.colors = newc
    
    def Ri(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['z'] = self.colors['y'] 
        newc['yi'] = self.colors['z']
        newc['zi'] = self.colors['yi']
        newc['y'] = self.colors['zi']
        newc['x'] = self.colors['x']
        self.colors = newc
    
    def Li(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['z'] = self.colors['yi'] 
        newc['y'] = self.colors['z']
        newc['zi'] = self.colors['y']
        newc['yi'] = self.colors['zi']
        newc['xi'] = self.colors['xi']
        self.colors = newc
    
    def Di(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['xi'] = self.colors['z'] 
        newc['zi'] = self.colors['xi']
        newc['x'] = self.colors['zi']
        newc['z'] = self.colors['x']
        newc['yi'] = self.colors['yi']
        self.colors = newc

    def Bi(self):
        newc = {'x': '-', 'y': '-', 'z': '-', 'xi': '-', 'yi':'-', 'zi': '-'}
        newc['x'] = self.colors['y'] 
        newc['yi'] = self.colors['x']
        newc['xi'] = self.colors['yi']
        newc['y'] = self.colors['xi']
        newc['zi'] = self.colors['zi']
        self.colors = newc



class Cube:
    def __init__(self):
        # starting solved position- Front:R, Up:W, Left:G, Right:B, Back:O, Down: Y -> https://rubikscu.be/
        self.grid = [
            [[Block(xi='G',y='W',z='R'), Block(y='W',z='R'), Block(x='B',y='W',z='R')], [Block(xi='G',y='W'), Block(y='W'), Block(x='B', y='W')], [Block(xi='G',y='W',zi='O'), Block(y='W',zi='O'), Block(x='B',y='W',zi='O')]], 
            [[Block(xi='G',z='R'), Block(z='R'), Block(x='B',z='R')], [Block(xi='G'), Block(), Block(x='B')], [Block(xi='G',zi='O'), Block(zi='O'), Block(x='B',zi='O')]], 
            [[Block(xi='G',yi='Y',z='R'), Block(yi='Y',z='R'), Block(x='B',yi='Y',z='R')], [Block(xi='G',yi='Y'), Block(yi='Y'), Block(x='B',yi='Y')], [Block(xi='G', yi='Y', zi='O'), Block(yi='Y', zi='O'), Block(x='B', yi='Y',zi='O')]]
        ]
        
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    self.grid[i][j][k].position = (i,j,k)
        self.U()

    def F(self):
        gridcopy = copy.deepcopy(self.grid)
        for i in range(3):
            for j in range(3):
                 gridcopy[j][0][2-i] = self.grid[i][0][j]

        for i in range(3):
            for j in range(3):
                gridcopy[i][0][j].F()
        
        self.grid = gridcopy


    def U(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[0][2-j][i] = self.grid[0][i][j]

        for i in range(3):
            for j in range(3):
                gridcopy[0][i][j].U()
        
        self.grid = gridcopy

    def R(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[i][2-j][2] = self.grid[j][i][2]

        for i in range(3):
            for j in range(3):
                gridcopy[j][i][2].R()
        
        self.grid = gridcopy


    def L(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[2-i][j][0] = self.grid[j][i][0]

        for i in range(3):
            for j in range(3):
                gridcopy[j][i][0].L()
        
        self.grid = gridcopy


    def D(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[2][j][2-i] = self.grid[2][i][j]

        for i in range(3):
            for j in range(3):
                gridcopy[2][i][j].D()
        
        self.grid = gridcopy
        

    def B(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[i][2][j] = self.grid[j][2][2-i]

        for i in range(3):
            for j in range(3):
                gridcopy[j][2][2-i].B()
        
        self.grid = gridcopy


    def Fi(self):
        gridcopy = copy.deepcopy(self.grid)
        for i in range(3):
            for j in range(3):
                 gridcopy[i][0][j] = self.grid[j][0][2-i]

        for i in range(3):
            for j in range(3):
                gridcopy[i][0][j].Fi()
        
        self.grid = gridcopy


    def Ui(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[0][i][j] = self.grid[0][2-j][i]

        for i in range(3):
            for j in range(3):
                gridcopy[0][i][j].Ui()
        
        self.grid = gridcopy

    def Ri(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[j][i][2] = self.grid[i][2-j][2]

        for i in range(3):
            for j in range(3):
                gridcopy[j][i][2].Ri()
        
        self.grid = gridcopy


    def Li(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[j][i][0] = self.grid[2-i][j][0]

        for i in range(3):
            for j in range(3):
                gridcopy[j][i][0].Li()
        
        self.grid = gridcopy


    def Di(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[2][i][j] = self.grid[2][j][2-i]

        for i in range(3):
            for j in range(3):
                gridcopy[2][i][j].Di()
        
        self.grid = gridcopy
        

    def Bi(self):
        gridcopy = copy.deepcopy(self.grid)

        for i in range(3):
            for j in range(3):
                 gridcopy[j][2][2-i] = self.grid[i][2][j]

        for i in range(3):
            for j in range(3):
                gridcopy[j][2][2-i].Bi()
        
        self.grid = gridcopy
        



c=Cube()

c.F()

print(c.grid)
# Ashith Farhan 79866
# Joel DSouza 79296
# Farooq Mirza 80205
# Sabbir Alam 79438
