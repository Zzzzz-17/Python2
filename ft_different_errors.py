def garden_operations(operation_number) -> None:
    """Depending on the operation number, a different error is raised."""

    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "seventeen" + 17
 

def test_error_types() -> None:
    """Demonstrates catching different errors and continuing execution."""

    print("Testing operation 0...")
    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as error:
        print(f"Caught ValueError: {error}")

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as error:
        print(f"Caught TypeError: {error}")

    print("Testing operation 4...")
    garden_operations(4)
    print("Operation completed successfully")    


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")