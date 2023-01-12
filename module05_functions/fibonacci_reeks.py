def fibonacci(hoeveel) -> list:
    fibonacci_sequence = [0,1]
    for x in range(hoeveel):
        n3 = (fibonacci_sequence[x] + fibonacci_sequence[x+1])
        fibonacci_sequence.append(n3)
    gulden_snede = fibonacci_sequence[-1] / fibonacci_sequence[-2]
    return fibonacci_sequence and gulden_snede

print(fibonacci(10))