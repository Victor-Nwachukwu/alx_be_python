def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except (ValueError, TypeError):
        return False, "Error: Please enter numeric values only."

    try:
        # Perform division, handling division by zero
        result = num / den
        return True, result  # FIXED: Return tuple (True, result)
    except ZeroDivisionError:
        return False, "Error: Cannot divide by zero."  # Return tuple (False, error)