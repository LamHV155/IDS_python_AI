class problem:
    def __init__(self, init, goal):
        self.__initialState = init
        self.__goalState = goal
        self.__actions = []
        

    
    def checkInvalid(self, x, y):
        if(x < 3 and x >= 0 and y < 3 and y >= 0):
            return True

    def getActions(self):
        return [[-1,0], [0,1], [1,0], [0,-1]] #UP, RIGHT, DOWN, LEFT



    def GoalTest(self, puzzle):
        if(self.__goalState == puzzle):
            return True
        return False
    
    def getInitialState(self):
        return self.__initialState