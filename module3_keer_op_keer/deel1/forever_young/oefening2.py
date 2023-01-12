from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
a = 1
while a < 10:
    robotArm.moveRight()
    a += 1
robotArm.drop()
b = 1
while b < 6:
    robotArm.moveLeft()
    b += 1
robotArm.grab()
c = 1
while c < 6:
    robotArm.moveRight()
    c += 1
robotArm.drop()
d = 1
while d < 3:
    robotArm.moveLeft()
    d += 1
robotArm.grab()
e = 1
while e < 3:
    robotArm.moveRight()
    e += 1
robotArm.drop()
    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()