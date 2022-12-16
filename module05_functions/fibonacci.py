
def fibonaci(hoeveel):
    nummers = 0,1
    if hoeveel in nummers:
        return hoeveel
    return fibonaci(hoeveel - 1) + fibonaci(hoeveel - 2)
    
        

for x in range(10):
    print(fibonaci(x))