def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except (ValueError, TypeError):
        return "Error: Please enter numeric values only."

    try:
        # Perform division, handling division by zero
        result = num / den
        return result  # FIXED: Return tuple (True, result)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."  # Return tuple (False, error)