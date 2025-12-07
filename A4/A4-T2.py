print("Program starting.")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))


for i in range(start, stop + 1):
    if (i != stop):
        print(i, end=" ")
    else:
        print(i)

print("Program ending.")
