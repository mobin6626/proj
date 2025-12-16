from dataclasses import dataclass

# -----------------------------
# Data structures
# -----------------------------
@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

@dataclass
class DAY_USAGE:
    weekday: str
    daily_usage: float
    daily_cost: float

# -----------------------------
# Constants
# -----------------------------
DELIMITER = ";"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday"]

# -----------------------------
# Read timestamps from file
# -----------------------------
def read_timestamps(filename: str) -> list[TIMESTAMP]:
    timestamps: list[TIMESTAMP] = []

    print(f'Reading file "{filename}".')
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                row = line.rstrip()
                if not row:
                    continue
                columns = row.split(DELIMITER)
                if len(columns) != 4:
                    continue
                ts = TIMESTAMP(
                    weekday=columns[0].strip(),
                    hour=columns[1].strip(),
                    consumption=float(columns[2].strip()),
                    price=float(columns[3].strip())
                )
                timestamps.append(ts)
    except FileNotFoundError:
        print(f'Error: file "{filename}" not found.')
    return timestamps

# -----------------------------
# Analyse timestamps (1-pass)
# -----------------------------
def analyse_timestamps(timestamps: list[TIMESTAMP]) -> list[DAY_USAGE]:
    print("Analysing timestamps.")
    # Initialize dictionary for quick lookup
    daily_dict = {day: DAY_USAGE(day, 0.0, 0.0) for day in WEEKDAYS}

    for ts in timestamps:
        if ts.weekday in daily_dict:
            daily = daily_dict[ts.weekday]
            daily.daily_usage += ts.consumption
            daily.daily_cost += ts.consumption * ts.price

    return list(daily_dict.values())

# -----------------------------
# Format results
# -----------------------------
def format_results(day_data: list[DAY_USAGE]) -> list[str]:
    print("Displaying results.")
    output: list[str] = []
    output.append("### Electricity consumption summary ###")
    for day in day_data:
        line = f" - {day.weekday} usage {day.daily_usage:.2f} kWh, cost {day.daily_cost:.2f} €"
        output.append(line)
    output.append("### Electricity consumption summary ###")
    return output

# -----------------------------
# Main program
# -----------------------------
def main():
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    timestamps = read_timestamps(filename)
    day_data = analyse_timestamps(timestamps)
    results = format_results(day_data)

    for line in results:
        print(line)

    print("Program ending.")

# -----------------------------
# Start program
# -----------------------------
main()
