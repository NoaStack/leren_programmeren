from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
for a in range(10):
    robotArm.grab()
    for x in range (5):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(5):
        robotArm.moveLeft()
    if a == 0 or a == 2 or a == 5:
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()