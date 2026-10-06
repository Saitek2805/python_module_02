#!/usr/bin/env python3
def garden_operations(operation_numer: int) -> None:
    try:
        print("Testing operation ", operation_numer,
              "...", sep="")
        if operation_numer == 0:
            string = "abc"
            int(string)
        if operation_numer == 1:
            42 / 0
        if operation_numer == 2:
            open("/non/existent/file", "r")
        if operation_numer == 3:
            print("uno" + 2)
    except ValueError as e:
        print("Caught ValueError:", e)
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    except TypeError as e:
        print("Caught TypeError:", e)
    else:
        print("Operation completed successfully")


def main() -> None:
    print("===  Garden Error Types Demo ===")
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
