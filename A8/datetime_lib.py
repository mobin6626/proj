from datetime import datetime

# Constants
MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday", 
    "Friday", "Saturday", "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    """
    Read timestamps from file and add to PTimestamps list.
    Timestamp format: YYYY-MM-DD HH:MM
    """
    PTimestamps.clear()  # Clear existing timestamps
    
    try:
        with open(PFilename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        # Parse timestamp: "2000-01-01 12:00"
                        timestamp = datetime.strptime(line, "%Y-%m-%d %H:%M")
                        PTimestamps.append(timestamp)
                    except ValueError:
                        print(f"Warning: Skipping invalid timestamp '{line}'")
        
        print(f"Read {len(PTimestamps)} timestamps from {PFilename}")
    
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found!")
    except Exception as e:
        print(f"Error reading file: {e}")

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    """Calculate amount of timestamps during given year."""
    count = 0
    for ts in PTimestamps:
        if ts.year == PYear:
            count += 1
    return count

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    """Calculate amount of timestamps during given month."""
    if PMonth not in MONTHS:
        return 0
    
    month_num = MONTHS.index(PMonth) + 1  # Convert to 1-12
    count = 0
    for ts in PTimestamps:
        if ts.month == month_num:
            count += 1
    return count

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    """Calculate amount of timestamps during given weekday."""
    if PWeekday not in WEEKDAYS:
        return 0
    
    weekday_num = WEEKDAYS.index(PWeekday)  # Monday=0, Sunday=6
    count = 0
    for ts in PTimestamps:
        if ts.weekday() == weekday_num:  # weekday() returns 0=Monday, 6=Sunday
            count += 1
    return count