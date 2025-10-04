def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except (ValueError, TypeError):
        return False, "Error: Please enter numeric values only."

    try:
        result = num / den
        return True, result
    except ZeroDivisionError:
        return False, "Error: Cannot divide by zero."
