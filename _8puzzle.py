from Week6.ProblemNode import NodePuzzle, problemPuzzle


def IDS(problem):                       
    for depth in range(1000000):        #vòng lặp độ sâu tìm kiếm từ 0 đến vô cùng (tạm cho bằng 1.000.000)
        result = DLS(problem, depth)    #gọi hàm DLS(Depth Limited Search) trả về 'cutoff' hoặc kết quả dưới dạng list
        if(result != 'cutoff'):         
            return result

def DLS(problem, limit):    # hàm DLS với tham số  đầu vào là problem và limit là depth của vòng lặp trong hàm IDS
    #Trả về hàm recursiveDLS cho giá trị là 'cutoff' hoặc kết quả dưới dạng list
    # NodePuzzle.Node(problem.getInitialState()) : object với state là init của problem
    return recursiveDLS(NodePuzzle.Node(problem.getInitialState()), problem, limit) 


def recursiveDLS(node, problem, limit):
    if(problem.GoalTest(node.getState())):      #Kiểm tra xem có là kết quả yêu cầu 
        return node.getListActions()            #nếu đúng trả về list các action của node đó
    elif(limit == 0):                           
        return 'cutoff'
    else:
        cutoff_occurred = False                 
        for action in problem.getActions():   
             #phương thức getActions() của problem sẻ trả về [[-1,0], [0,1], [1,0], [0,-1]] tương ứng với UP, RIGHT, DOWN, LEFT
            
            pos0 = node.getPos0()
            #Phương thức getPos0() trả vể vị trí x, y của ô trống trong state thuộc node dưới dạng [x,y]
           
            if(problem.checkInvalid(pos0[0] + action[0], pos0[1] + action[1])):
            #Phương thức checkInvalid(x,y) kiểm tra vị trí sau khi dịch chuyển ô trống có nằm trong khoảng cho phép hay không 
                
                newState = node.createNewState(pos0, action)
                #Tạo state mới với vị trí ô trống hiện tại và action hợp lệ
               
                child = NodePuzzle.Node(newState, node, action) #Tạo node con 
               
                result = recursiveDLS(child, problem, limit-1) #gọi lại hàm  recursiveDLS với limit giảm dần
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

def convert(list):
    if(len(list) == 0):
        return []
    action = []
    list.pop(0)
    for x in list:
        if(x == [-1,0]):
            action.append('UP')
        elif(x == [1,0]):
            action.append('DOWN')
        elif(x == [0,-1]):
            action.append('LEFT')
        elif(x == [0,1]):
            action.append('RIGHT')
    return action
        

print(convert(IDS(problem)))