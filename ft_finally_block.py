class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)
       

def water_plant(plant_name) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")    

def test_watering_system() -> None:

    try:
        print("\nTesting valid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")  
    finally:
        print("Closing watering system")

    try:
        print("\nTesting invalid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")  
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")

    
if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
