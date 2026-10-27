def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:

    try:
        print(f"Input data is '{temp_str}'")
        result = input_temperature(temp_str)
        print(f"Temperature is now {result}°C")
        print()
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
        print()


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature("25")
    test_temperature("abc")
    print("All tests completed - program didn't crash!")