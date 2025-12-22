import copy
import time
from typing import Callable, List

def readValues(PValues: List[int]) -> None:
    PValues.clear()
    filename = input("Insert dataset filename: ")
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                val = line.strip()
                if val:
                    PValues.append(int(val))
        print()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.\n")

def bubbleSort(PNums: List[int]) -> List[int]:
    arr = PNums.copy()
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quickSort(PNums: List[int]) -> List[int]:
    if len(PNums) <= 1:
        return PNums.copy()
    pivot = PNums[len(PNums)//2]
    left = [x for x in PNums if x < pivot]
    middle = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x > pivot]
    return quickSort(left) + middle + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: List[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    return EndTime - StartTime

def main() -> None:
    print("Program starting.")
    
    Values: List[int] = []
    Results: List[str] = []
    filename = ""
    
    while True:
        print("\nOptions:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "0":
            print("Exiting program.\n")
            break
        
        elif choice == "1":
            readValues(Values)
            if Values:
                filename = "dataset"  # You can track the actual filename
        
        elif choice == "2":
            if not Values:
                print("Error: No dataset loaded.\n")
                continue
            
            print(f"Measured speeds for dataset (size: {len(Values)}):")
            
            BuiltinSortedTimeNs = measureSortingTime(sorted, copy.deepcopy(Values))
            BubbleSortTimeNs = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            QuickSortTimeNs = measureSortingTime(quickSort, copy.deepcopy(Values))
            
            Results = [
                f"Measured speeds for dataset (size: {len(Values)}):",
                f" - Built-in sorted {BuiltinSortedTimeNs} ns",
                f" - Bubble sort {BubbleSortTimeNs} ns",
                f" - Quick sort {QuickSortTimeNs} ns"
            ]
            
            for line in Results:
                print(line)
            print()
        
        elif choice == "3":
            if not Results:
                print("Error: No results to save.\n")
                continue
            
            results_file = input("Insert results filename: ")
            try:
                with open(results_file, 'w') as f:
                    for line in Results:
                        f.write(line + '\n')
                print(f"\nResults saved to {results_file}\n")
            except Exception as e:
                print(f"Error saving file: {e}\n")
        
        else:
            print("Invalid choice.\n")
    
    Values.clear()
    Results.clear()
    print("Program ending.")

main()