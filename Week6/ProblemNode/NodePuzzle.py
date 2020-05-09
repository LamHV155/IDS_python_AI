import copy 

class Node:

    def __init__(self, state, parent=None, action='Init'):
        self.__state = state
        self.__parent = parent
        self.__action = []
        

        if(self.__parent is not None):
            self.__action = copy.deepcopy(self.__parent.getListActions())
        self.__action.append(action)
        
            


    def createNewState(self, curPos0, action):
        state = copy.deepcopy(self.__state)
        if(action == [0,-1]): #LEFT
            state[curPos0[0]][curPos0[1]], state[curPos0[0]][curPos0[1]-1] = state[curPos0[0]][curPos0[1]-1], state[curPos0[0]][curPos0[1]]
            return state 
        elif(action == [0,1]): #RIGHT
            state[curPos0[0]][curPos0[1]], state[curPos0[0]][curPos0[1]+1] = state[curPos0[0]][curPos0[1]+1], state[curPos0[0]][curPos0[1]]
            return state 
        elif(action == [-1,0]): #UP
            state[curPos0[0]][curPos0[1]], state[curPos0[0]-1][curPos0[1]] = state[curPos0[0]-1][curPos0[1]], state[curPos0[0]][curPos0[1]]
            return state 
        elif(action == [1,0]): #DOWN
            state[curPos0[0]][curPos0[1]], state[curPos0[0]+1][curPos0[1]] = state[curPos0[0]+1][curPos0[1]], state[curPos0[0]][curPos0[1]]
            return state 

    def getPos0(self):
        for x in  range(3):
            for y in range(3):
                if(self.__state[x][y] == 0):
                    return [x,y]


    def getListActions(self):
        return self.__action
    
    def getState(self):
        return self.__state