from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
b = 0
while b < 4:
    a = 0
    if a == 0:
        robotArm.grab()
    while a < 9:
        robotArm.moveRight()
        a += 1
    if a == 9:
        robotArm.drop()
    c = 0
    while c < 9:
        robotArm.moveLeft()
        c += 1
    b += 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()