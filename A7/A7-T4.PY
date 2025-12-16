from dataclasses import dataclass

# -----------------------------
# Data structure
# -----------------------------
@dataclass
class Timestamp:
    weekday: str
    hour: str
    consumption: float
    price: float


# -----------------------------
# Constants
# -----------------------------
DELIMITER = ";"


# -----------------------------
# Read timestamps from file
# -----------------------------
def read_timestamps(filename: str) -> list[Timestamp]:
    timestamps: list[Timestamp] = []

    print(f'Reading file "{filename}".')

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                row = line.rstrip()

                # Skip empty lines
                if not row:
                    continue

                columns = row.split(DELIMITER)
                if len(columns) != 4:
                    print(f"Warning: invalid row skipped → {row}")
                    continue

                ts = Timestamp(
                    weekday=columns[0].strip(),
                    hour=columns[1].strip(),
                    consumption=float(columns[2].strip()),
                    price=float(columns[3].strip())
                )

                timestamps.append(ts)
                columns.clear()

    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')

    return timestamps


# -----------------------------
# Main program
# -----------------------------
def main():
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    timestamps = read_timestamps(filename)

    if not timestamps:
        print("No timestamp data available.")
        print("Program ending.")
        return

    print("Electricity usage:")

    total_consumption = 0.0
    total_cost = 0.0

    for ts in timestamps:
        cost = ts.price * ts.consumption
        total_consumption += ts.consumption
        total_cost += cost

        print(f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, "
              f"consumption {ts.consumption:.2f} kWh, total {cost:.2f} €")

    # Optionally print totals (not required, but common)
    # print(f"\nTotal consumption: {total_consumption:.2f} kWh")
    # print(f"Total cost: {total_cost:.2f} €")

    print("Program ending.")


# Start
main()
