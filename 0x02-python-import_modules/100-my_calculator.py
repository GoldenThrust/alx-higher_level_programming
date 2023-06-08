#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys as s

    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(s.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        s.exit(1)

    if s.argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        s.exit(1)

    a = int(s.argv[1])
    b = int(s.argv[3])
    print("{} {} {} = {}".format(a, s.argv[2], b, operators[s.argv[2]](a, b)))
