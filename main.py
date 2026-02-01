from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator


#run terminal to find error code for pygame and numpy for simulator and then copy and paste error code in google so then you can fix it(depends on what kind of computer)
def idle(): 
    robot.motors(left=FORWARD, right=FORWARD, seconds=0)

def wall_check(left, right): #add after like 10 times of bouncing off wall to change state to idle 
    if left <3 and right <3: 
        print ( "too close, go backward and stop")
        robot.motors(left=STOP, right=STOP, seconds=0.1)
        robot.motors(left=BACKWARD, right=BACKWARD, seconds=0.5)
        robot.motors(left=BACKWARD, right=FORWARD, seconds=1.5401) 
        return "stop" 
    elif left <5: 
        print ( "turn right")
        robot.motors(left=STOP, right=STOP, seconds=0.1)
        robot.motors(left=BACKWARD, right=BACKWARD, seconds=0.5)
        robot.motors(left=BACKWARD, right=FORWARD, seconds=1.5401) #rotate away from wall(going left)
    elif right<5:
        print ( "turn left")
        robot.motors(left=STOP, right=STOP, seconds=0.1)
        robot.motors(left=BACKWARD, right=BACKWARD, seconds=0.5)
        robot.motors(left=FORWARD, right=BACKWARD, seconds=1.5401) #rotate away from wall(going right)
    else:
        print ( "continue")
    
    return "continue"

def follow_wall():
    order = "continue"

    while order!="stop":
        robot.motors(left=FORWARD,right=FORWARD, seconds=0.1)
        right_distance=robot.right_sonar()
        left_distance=robot.left_sonar()
        print(f"left / right distance {left_distance} {right_distance} ")

        order = wall_check( left_distance, right_distance )

#        if left_distance <25 and right_distance<25:
#            print ( "go back then turn 180")
#            robot.motors(left=STOP, right=STOP, seconds=0.1)
#            robot.motors(left=BACKWARD, right=BACKWARD, seconds=1)
#            robot.motors(left=FORWARD, right=BACKWARD, seconds=1.2) 
#        elif left_distance <25:
#            print ( "turn right")
#            robot.motors(left=STOP, right=STOP, seconds=0.1)
#            robot.motors(left=BACKWARD, right=BACKWARD, seconds=0.5)
#            robot.motors(left=BACKWARD, right=FORWARD, seconds=1.4) #rotate away from wall(going left)
#        elif right_distance<25:
#            print ( "turn left")
#            robot.motors(left=STOP, right=STOP, seconds=0.1)
#            robot.motors(left=BACKWARD, right=BACKWARD, seconds=0.5)
#            robot.motors(left=FORWARD, right=BACKWARD, seconds=1.4) #rotate away from wall(going right)
#        else:
#            print ( "continue")




def left_circle_draw():
    for i in range(360):
        robot.motors(left=FORWARD,right=FORWARD, seconds=0.01)
        robot.motors(left=BACKWARD, right=FORWARD, seconds=0.01)
        wall_check( robot.left_sonar(), robot.right_sonar() )
def right_circle_draw():
    for i in range(360):
        robot.motors(left=FORWARD,right=FORWARD, seconds=0.01)
        robot.motors(left=FORWARD, right=BACKWARD, seconds=0.01)
        wall_check( robot.left_sonar(), robot.right_sonar() )

def both_forward(): 
    robot.motors(left=FORWARD,right=FORWARD, seconds=2)
    wall_check( robot.left_sonar(), robot.right_sonar() )

def figure_eight():
    left_circle_draw()
    right_circle_draw()

def right_donut():
    robot.motors(left=FORWARD, seconds=5)
    wall_check( robot.left_sonar(), robot.right_sonar() )

def left_donut():
    robot.motors(right=FORWARD, seconds=5)
    wall_check( robot.left_sonar(), robot.right_sonar() )

def right_spin():
    robot.motors(right=FORWARD, left=-BACKWARD, seconds=1.525)
    wall_check( robot.left_sonar(), robot.right_sonar() )
    
def left_spin():
    robot.motors(right=-FORWARD, left=BACKWARD, seconds=1.525)
    wall_check( robot.left_sonar(), robot.right_sonar() )

def angle_supp():
    robot.motors(left=FORWARD, right=FORWARD, seconds=2 )
    robot.motors(left=FORWARD, right=BACKWARD, seconds=1.84812)

def angle_internal():
    robot.motors(left=FORWARD, right=FORWARD, seconds=2)
    robot.motors(left=BACKWARD, right=FORWARD, seconds=2.4416) #0.16604=36degrees

def star():
    for i in range(5):
        #wall_check( robot.left_sonar(), robot.right_sonar() )

        # robot moves in a spike shape
        robot.motors(left=FORWARD, right=FORWARD, seconds=2 )
        robot.motors(left=FORWARD, right=BACKWARD, seconds=1.84812)
        #robot.motors(left=BACKWARD, right=FORWARD, seconds=1.84812)
        robot.motors(left=FORWARD, right=FORWARD, seconds=2)

        # robot changes angle for next spike
        robot.motors(left=BACKWARD, right=FORWARD, seconds=2.4416) #0.16604=36degrees
        #robot.motors(left=FORWARD, right=BACKWARD, seconds=2.4416) #0.16604=36degrees
        
        #angle_supp()
        #angle_internal()

robot_state="idle"

while robot_state!="off":
    robot_state = input("What would you like the robot to do? (check wall,idle,follow wall,off,8, or star)")
    if robot_state=="check wall":
        print("The state is check wall")
        wall_check( robot.left_sonar(), robot.right_sonar() )
    elif robot_state=="idle":
        print("The state is idle")
        idle()
    elif robot_state=="follow wall":
        print("The state is follow wall")
        follow_wall()
    elif robot_state=="off":
        print("robot terminated")
        break
    elif robot_state=="8":
        print("The state is eight")
        figure_eight()
    elif robot_state=="star":
        print("star")
        star()
    else:
        print(f"Error! The state {robot_state} does not exist")

robot.exit()
