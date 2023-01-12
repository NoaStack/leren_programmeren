from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
a = 9
for x in range(5):
    robotArm.grab()
    for x in range(a):
        robotArm.moveRight()
    a -= 1
    robotArm.drop()
    for x in range(a):
        robotArm.moveLeft()
    a -= 1
        


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()