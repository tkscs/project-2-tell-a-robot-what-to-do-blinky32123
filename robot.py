from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator

 
#run terminal to find error code for pygame and numpy for simulator and then copy and paste error code in google so then you can fix it(depends on what kind of computer)
def idle():# replace with break function so a loop isnt needeD?
    robot.motors(left=FORWARD, right=FORWARD, seconds=0)

    


robot.exit()