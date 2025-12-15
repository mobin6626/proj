def askDimension(PPrompt: str) -> float:
    value = input(f"Insert-{PPrompt}: ")
    return float(value)

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    return PWidth * PHeight

def main():
    print("Program-starting.\n")
    
    width = askDimension("width")
    height = askDimension("height")
    
    area = calcRectangleArea(width, height)
    print(f"Area-is-{area:.2f}")
    
    print("Program-ending.")
    return None

main()
