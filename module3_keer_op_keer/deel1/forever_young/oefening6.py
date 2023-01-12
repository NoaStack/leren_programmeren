from turtle import left
from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
a = 0
while a < 4:
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
        a +=1
    



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()