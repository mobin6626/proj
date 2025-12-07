print("Program starting.")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

while(start <= stop):
    if (start != stop):
        print(start,end=" ")
        
    else:
        print(start)
    start += 1

print("Program ending.")
