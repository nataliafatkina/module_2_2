# input data
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# program

if first == second == third:
    print(3)
elif first == second != third or first != second == third or first == third != second:
    print(2)
else: print(0)