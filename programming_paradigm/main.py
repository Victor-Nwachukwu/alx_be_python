#!/usr/bin/env python3
"""
Robust Division Calculator - Command Line Interface
Refactored version with proper error handling
"""

import sys
from robust_division_calculator import safe_divide

def main():
    # Validate command line arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>", file=sys.stderr)
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Use the safe_divide function correctly (it returns a tuple)
    success, result = safe_divide(numerator, denominator)
    
    if success:
        print(f"The result of the division is {result}")
    else:
        print(result, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()