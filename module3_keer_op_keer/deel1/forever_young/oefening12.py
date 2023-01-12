from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 1
a = 0
while a < 9:
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "red":
        for x in range(9 - a):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(8 - a):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    a += 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()