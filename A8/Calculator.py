def add(PAddend1: float, PAddend2: float) -> float:
    """Return the sum of two numbers."""
    return PAddend1 + PAddend2

def subtract(PMinuend: float, PSubtrahend: float) -> float:
    """Return the difference between two numbers."""
    return PMinuend - PSubtrahend

def multiply(PMultiplicant: float, PMultiplier: float) -> float:
    """Return the product of two numbers."""
    return PMultiplicant * PMultiplier

def divide(PDividend: float, PDivisor: float) -> float:
    """Return the quotient of two numbers."""
    if PDivisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return PDividend / PDivisor