#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError(temp_str + "ºC is too hot for plants (max 40°C)")
    if temp_int < 0:
            raise ValueError(temp_str + "ºC is too cold for plants (min 0°C)")
    return temp_int

def test_temperature() -> None:
    try:
        temp_str = "25"
        print("\nInput data is '", temp_str, "'", sep="")
        input_temperature(temp_str)
    except ValueError:
        print("Caught input_temperature error: ",
              "invalid literal for int() with base 10: '",
              temp_str, "'", sep="")
    else:
        print("Temperature is now ", temp_str,"ºC", sep="")
    try:
        temp_str = "abc"
        print("\nInput data is '", temp_str, "'", sep="")
        input_temperature(temp_str)
    except ValueError:
        print("Caught input_temperature error: ",
              "invalid literal for int() with base 10: '",
              temp_str, "'", sep="")
    else:
        print("Temperature is now ", temp_str,"ºC", sep="")
    try:
        temp_str = "100"
        print("\nInput data is '", temp_str, "'", sep="")
        input_temperature(temp_str)
    except ValueError as e:
        print("Caught input_temperature error:",
              e)
    else:
        print("Temperature is now ", temp_str,"ºC", sep="")
    try:
        temp_str = "-50"
        print("\nInput data is '", temp_str, "'", sep="")
        input_temperature(temp_str)
    except ValueError as e:
        print("Caught input_temperature error:",
              e)
    else:
        print("Temperature is now ", temp_str,"ºC", sep="")

def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    main()