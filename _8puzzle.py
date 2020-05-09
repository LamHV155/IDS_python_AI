from Week6.ProblemNode import NodePuzzle, problemPuzzle


def IDS(problem):
    for depth in range(1000000):
        result = DLS(problem, depth)
        if(result != 'cutoff'):
            return result

def DLS(problem, limit):
    return recursiveDLS(NodePuzzle.Node(problem.getInitialState()), problem, limit)


def recursiveDLS(node, problem, limit):
    if(problem.GoalTest(node.getState())):
        return node.getListActions()
    elif(limit == 0):
        return 'cutoff'
    else:
        cutoff_occurred = False
        for action in problem.getActions():
            if(problem.checkInvalid(node.getPos0()[0] + action[0], node.getPos0()[1] + action[1])):
                newState = node.createNewState(node.getPos0(), action)
                child = NodePuzzle.Node(newState, node, action)
                result = recursiveDLS(child, problem, limit-1)
                if(result == 'cutoff'):
                    cutoff_occurred = True
                elif(result != []):
                    return result
        if(cutoff_occurred):
            return 'cutoff'
        else: 
            return []


init = [[3,1,2],[6,0,8],[7,5,4]]
goal = [[0,1,2],[3,4,5],[6,7,8]]

problem = problemPuzzle.problem(init, goal)

print(IDS(problem))