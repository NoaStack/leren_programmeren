from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
i = 1
while i < 10:
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "white":
        robotArm.moveRight()
        robotArm.drop()
        i += 1
    else:
        robotArm.drop()
    robotArm.moveRight()
    i += 1
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
