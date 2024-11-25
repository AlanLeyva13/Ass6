import sys

def validate_input(integers):
    """
    Valida la entrada para garantizar que contenga solo números enteros.
    Si la validación falla, el script sale con un mensaje de error.
    """
    try:
        return [int(x) for x in integers.split(",")]
    except ValueError:
        print("Error: Input contains non-integer values.")
        sys.exit(1)

def bitwise_operations_and(numbers):
    result_and = numbers[0]    
    for num in numbers[1:]:
        result_and &= num    
    return result_and

def bitwise_operations_or(numbers):
    result_or = numbers[0]    
    for num in numbers[1:]:
        result_or |= num    
    return result_or

def bitwise_operations_xor(numbers):
    result_xor = numbers[0]    
    for num in numbers[1:]:
        result_xor ^= num    
    return result_xor

def filter_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]

def main():
    if len(sys.argv) < 3:
        print("Error: Missing input or threshold.")
        print("Usage: python script.py 'num1,num2,num3' threshold")
        print("Example: python script.py '1,2,3,4,5' 3")
        sys.exit(1)

    integers = sys.argv[1]
    try:
        threshold = int(sys.argv[2])
    except ValueError:
        print("Error: Threshold must be an integer.")
        sys.exit(1)

    numbers = validate_input(integers)
    result_and = bitwise_operations_and(numbers)
    result_or = bitwise_operations_or(numbers)
    result_xor = bitwise_operations_xor(numbers)

    filtered_numbers = filter_numbers(numbers, threshold)
    print(f"Integers separated by commas: {numbers}")
    print(f"Threshold: {threshold}")
    print(f"bitwise operation:")
    print(f"Bitwise AND: {result_and}")
    print(f"Bitwise OR: {result_or}")
    print(f"Bitwise XOR: {result_xor}")
    print(f"Numbers greater than threshold: {filtered_numbers}")

if __name__ == "__main__":
    main()