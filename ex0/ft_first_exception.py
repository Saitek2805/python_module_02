#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)

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

def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    main()