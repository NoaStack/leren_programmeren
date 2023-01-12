from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
b = 0
while b < 5:
    a = 0
    if a == 0:
        robotArm.grab()
    while a < 2:
        robotArm.moveRight()
        a += 1
    if a == 2:
        robotArm.drop()
    c = 0
    while c < 2:
        robotArm.moveLeft()
        c += 1
    b += 1

d = 0
robotArm.moveRight()


while d < 5:
    e = 0
    while e < 7:
        robotArm.moveRight()
        e += 1
    if e == 1:
        robotArm.grab()
    f = 0
    while f < 1:
        robotArm.moveLeft()
        f += 1
    if f == 1:
        robotArm.drop()
    d += 1




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()