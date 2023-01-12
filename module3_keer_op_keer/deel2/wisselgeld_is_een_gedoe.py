# name of student: Noa
# number of student: 99070686
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # What you have to pay
paid = int(float(input('Paid amount: ')) * 100) # What you already paid and gave
change = paid - toPay #

if change > 0: # If u need to return coins make it go through
  coinValue = 500 # Changes the value to the first 
  
  while change > 0 and coinValue > 0: # 
    nrCoins = change // coinValue #

    if nrCoins > 0: # if number coins bigger then 0 run this
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # print what u can return max of
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # put in how many coins u need to return
      (f"Gave {nrCoinsReturned} of {coinValue / 100} euros")# how many coins u returned
      change -= nrCoinsReturned * coinValue # how many returned
    

# comment on code below: makes it go through the cylce of going from 5 euros to 1 cent of returning
    if coinValue == 500:
        coinValue = 200 
    elif coinValue == 200:
        coinValue = 100
    elif coinValue == 100:
        coinValue = 50
    elif coinValue == 50:
        coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # If u need to return more coins then print how much u have to return
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
  