WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturnday", "Sunday"
)

def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')
    PRows.clear()

    try:
        with open(PFilename, "r", encoding="utf-8") as f:
            first = True
            for line in f:
                if first:
                    first = False     # skip header
                    continue

                if line == "\n":      # empty row → skip
                    continue

                PRows.append(line.strip("\n"))

    except FileNotFoundError:
        print("Error: File not found.")
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()

    WeekdayTimestampAmount = [0] * 7

    for row in PRows:
        for i, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                WeekdayTimestampAmount[i] += 1
                break

    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {WeekdayTimestampAmount[i]} stamps")
    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for r in PResults:
        print(r)
    print("### Timestamp analysis ###")
    return None


def main() -> None:
    print("Program starting.")

    Rows: list[str] = []
    Results: list[str] = []

    filename = input("Insert filename: ").strip()

    readFile(filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)

    Rows.clear()
    Results.clear()
    print("Program ending.")
    return None


main()
