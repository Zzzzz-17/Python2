class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown watering error"):
        super().__init__(message)


def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    print("\nTesting PlantError...")
    try:
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        test_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        test_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_errors()
    print("\nAll custom error types work correctly!")
