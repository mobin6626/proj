print("Program starting.")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))
if (inspection > start and inspection < stop):
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if i == inspection:
            break
        print(i, end=" ")
    print()

    print("Second loop - inspection with continue:")
    for i in range(start, stop):
        if i == inspection:
            continue
        print(i, end=" ")
    print()

    print("Program ending.")
else:
    print("Error")