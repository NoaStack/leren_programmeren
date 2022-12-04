import random

namen = ['nam1', 'naam2', 'naam3']
loten = {}
keys = []
values = []


def test():
    while len(loten) != len (namen):
        if len(namen) - len(loten) == 2:
            for i in namen:
                for j in namen:
                    if i not in loten.keys():
                        if j not in  loten.values():
                            loten[i] = j
        for naam in namen:
            randomNaam = random.choice(namen)
            if naam != randomNaam and naam not in keys and randomNaam not in values:
                loten[naam] = randomNaam
                keys.append(naam)
                values.append(randomNaam)
            

        print(loten)

    for i, j in loten.items():
        print(i.capitalize() , 'heeft', j.capitalize(), 'getrokken!')
    if i == j:
        print("oef")
        
for i in range(10000):
    test()
    print(f'------------{i}------------')
    
