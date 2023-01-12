from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
for x in range (7):
    robotArm.grab()
    for x in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(8):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()