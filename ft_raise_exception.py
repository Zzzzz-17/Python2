def input_temperature(temp_str: str) -> int:
    
    temp = int(temp_str)

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature() -> None:

    test_values = ["25", "abc", "100", "-50"]

    for temp_str in test_values:
        try:
            print(f"Input data is '{temp_str}'")
            result = input_temperature(temp_str)
            print(f"Temperature is now {result}°C")
            print()
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
            print()

if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")