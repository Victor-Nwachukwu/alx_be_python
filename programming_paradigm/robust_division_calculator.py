def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."  # when denominator is 0
    
    except ValueError:
        return "Error: Please enter numeric values only."  # when conversion to float fails