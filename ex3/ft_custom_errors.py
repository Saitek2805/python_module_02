#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, *arg: str) -> None:
        default_message = "Unkown garden error"
        if arg:
            super().__init__(*arg)
        else:
            super().__init__(default_message)


class PlantError(GardenError):
    def __init__(self, *arg: str) -> None:
        default_message = "Unkown plant error"
        if arg:
            super().__init__(*arg)
        else:
            super().__init__(default_message)


class WaterError(GardenError):
    def __init__(self, *arg: str) -> None:
        default_message = "Unkown water error"
        if arg:
            super().__init__(*arg)
        else:
            super().__init__(default_message)


def raise_garden_error(number: int) -> None:
    try:
        if number == 1:
            raise GardenError("The tomato plant is wilting!")
        elif number == 2:
            raise GardenError("Not enough water in the tank")
        else:
            raise GardenError
    except GardenError as e:
        print("Caught GardenError:", e)


def raise_plant_error(number: int) -> None:
    try:
        if number:
            raise PlantError("The tomato is wiltering")
        else:
            raise PlantError
    except PlantError as e:
        print("Caught PlantError:", e)


def raise_water_error(number: int) -> None:
    try:
        if number:
            raise WaterError("Not enough water in the tank")
        else:
            raise WaterError
    except WaterError as e:
        print("Caught PlantError:", e)


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    raise_plant_error(1)
    print("\nTesting WaterError...")
    raise_water_error(1)
    print("\nTesting catching all garden errors...")
    raise_garden_error(1)
    raise_garden_error(2)


if __name__ == "__main__":
    main()
