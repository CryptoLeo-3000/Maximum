def find_max():
    numbers = [10, 7,3,6,5,1]
    Max = numbers[0]
    for i in numbers:
        if i >= Max:
            Max = i
    print(f"Maximum number = {Max}")