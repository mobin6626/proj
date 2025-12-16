def readValues(filename):
    values = []

    with open(filename, "r") as file:
        for line in file:
            num = line.strip()
            if num != "":
                values.append(int(num))

    return values


def analyseNumbers(nums):
    count_val = len(nums)
    sum_val = sum(nums)
    greatest_val = max(nums)
    average_val = sum_val / count_val

    return count_val, sum_val, greatest_val, average_val


def main():
    print("Program starting.")

    filename = input("Insert filename: ")

    print("#### Number analysis START ####")
    print(f'File "{filename}" results:')

    nums = readValues(filename)
    count_val, sum_val, greatest_val, average_val = analyseNumbers(nums)

    print("Count;Sum;Greatest;Average")
    print(f"{count_val};{sum_val};{greatest_val};{average_val:.2f}")

    print("#### Number analysis END ####")
    print("Program ending.")

main()
