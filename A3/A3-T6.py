print("UNIT CONVERSION PROGRAM")

while True:
    print("\n1: Meters to Kilometers")
    print("2: Kilometers to Meters")
    print("3: Grams to Pounds")
    print("4: Pounds to Grams")
    print("5: Exit")
    
    choice = input("Choose (1-5): ")
    
    if choice == '1':
    
        m = float(input("Meters: "))
        km = m / 1000
        print(f"Result: {round(km, 1)} km")

    elif choice == '2':
        
        km = float(input("Kilometers: "))
        m = km * 1000
        print(f"Result: {round(m, 1)} m")
    
    elif choice == '3':
    
        g = float(input("Grams: "))
        lb = g / 453.59237
        print(f"Result: {round(lb, 1)} lb")
    elif choice == '4':
        
        lb = float(input("Pounds: "))
        g = lb * 453.59237
        print(f"Result: {round(g, 1)} g")
    
    elif choice == '5':
        print("Exiting...")
        break
    
    else:
        print("Unknown option.")