#!/usr/local/bin/python3
import sys


def print_usage():
    print("*" * 50)
    print("\nf2c Fahrenheit to Celsius Conversion")
    print("Usage: f2c <temperature>\n")
    print("*" * 50)


def input_is_valid(num):
    try:
        n = float(num)
        return True
    except ValueError:
        print('Invalid temperature provided.')
        return False


def convert(temp):
    if not input_is_valid(temp):
        print_usage()
        exit(0)
    else:
        c = ((float(temp) - 32) * 5) / 9
        formatted_c = "{:.2f}".format(c)
        print("{}°F is {}°C".format(temp, formatted_c))
        exit(0)


def main():
    if len(sys.argv) == 2:
        convert(sys.argv[1])
    else:
        print_usage()
        exit(0)


if __name__ == "__main__":
    main()
