from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 1
i = 1
a = robotArm.scan()
while i < 10:
    robotArm.grab()
    b = robotArm.scan()
    if b == "":
        break
    else:
        for x in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(i):
            robotArm.moveLeft()
    i += 1
    
    # idee maak een stapel en daarna
    

        

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()