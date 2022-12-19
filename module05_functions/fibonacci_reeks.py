def fibonacci(nmr:int):
    if nmr <= 1:
        return nmr
    else:
        return(fibonacci(nmr-1)) + fibonacci((nmr-2))

teller = 10

for i in range(teller):
    print(fibonacci(nmr=i))
    