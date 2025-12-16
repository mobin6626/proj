def main():
    print("Program starting.")

    Source = input("Insert Source: ")
    Destination = input("Insert Destination: ")

    src = open(Source, "r")
    src = src.read()
    des = open(Destination, "w")
    copy = des.write(src + "\n")

    print("Program ending.")
    return None

main()
