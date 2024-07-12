class TestCalculations:
    """
    A test class for the calculations module.

    This class is designed to contain unit tests for the functions defined in the calculations module,
    including add, subtract, multiply, and divide. Each method within this class should test a specific
    function from the calculations module for correctness, handling of edge cases, and error conditions.
    """
    def __init__(self):
        """
        Initializes the TestCalculations class.

        This constructor can be used to set up any prerequisites for the tests,
        such as initializing variables or setting up test data.
        """
        print("Initializing TestCalculations Class...")

def add(a, b):
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a (float): A number representing the first addend in the addition.
        b (float): A number representing the second addend in the addition.

    Returns:
        num (float): A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a, b):
    """Compute and return the difference between two numbers.

    Examples:
        >>> subtract(6.0, 4.0)
        2.0
        >>> subtract(10, 3)
        7.0

    Args:
        a (float): A number representing the minuend in the subtraction.
        b (float): A number representing the subtrahend in the subtraction.

    Returns:
        num (float): A number representing the arithmetic difference between `a` and `b`.
    """
    return float(a - b)

def multiply(a, b):
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(3.0, 2.0)
        6.0
        >>> multiply(7, 5)
        35.0

    Args:
        a (float): A number representing the multiplicand in the multiplication.
        b (float): A number representing the multiplier in the multiplication.

    Returns:
        num (float): A number representing the arithmetic product of `a` and `b`.
    """
    return float(a * b)

def divide(a, b):
    """Compute and return the quotient of two numbers.

    Examples:
        >>> divide(8.0, 2.0)
        4.0
        >>> divide(9, 3)
        3.0
        >>> divide(10, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero

    Args:
        a (float): A number representing the dividend in the division.
        b (float): A number representing the divisor in the division.

    Raises:
        ZeroDivisionError: If `b` is zero, indicating division by zero is not allowed.

    Returns:
        num (float): A number representing the arithmetic quotient of `a` divided by `b`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)

if __name__ == "__main__":
    print(f"2 + 4 = {add(2, 4)}")
    print(f"6 - 3 = {subtract(6, 3)}")
    print(f"5 * 7 = {multiply(5, 7)}")
    print(f"8 / 2 = {divide(8, 2)}")
    myTestCalc = TestCalculations()