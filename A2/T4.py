print("program starting")
print("..Estimate how many minutes you spent on programming")
A1_T1 = int(input("A1_T1: "))
A1_T2 = int(input("A1_T2: "))
A1_T3 = int(input("A1_T3: "))
A1_T4 = int(input("A1_T4: "))
A1_T5 = int(input("A1_T5: "))
A1_T6 = int(input("A1_T6: "))
A1_T7 = int(input("A1_T7: "))
total = A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7
print(f"in total you spent {total} min on programming")
print(f"average per task was {round(total / 7, 2)} min and same rounded to the nearest integer {round(total/7)}")
print("program ending")

