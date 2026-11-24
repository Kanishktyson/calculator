"""A simple command-line calculator.

Usage:
    python calculator.py

Type expressions like `2 + 3 * 4`... well, almost — one operator at a time:
    calc> 2 + 3
    = 5.0

Supported operators: +  -  *  /  %  **
Type 'quit' to exit.
"""
import operator

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "**": operator.pow,
}


def evaluate(a: float, op: str, b: float) -> float:
    """Apply one operator to two numbers."""
    if op not in OPERATORS:
        raise ValueError(f"Unknown operator: {op!r}")
    if op in ("/", "%") and b == 0:
        raise ZeroDivisionError("Cannot divide or take modulo by zero")
    return OPERATORS[op](a, b)


def parse(text: str):
    """Split an input line into (left, operator, right)."""
    parts = text.split()
    if len(parts) != 3:
        raise ValueError("Format: <number> <operator> <number>   e.g.  2 + 3")
    a, op, b = parts
    try:
        a, b = float(a), float(b)
    except ValueError:
        raise ValueError(f"Couldn't read numbers from: {a!r} {b!r}")
    return a, op, b


def main() -> None:
    print("Simple Calculator — supported: + - * / % **   (type 'quit' to exit)")
    while True:
        try:
            line = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if line.lower() in ("q", "quit", "exit"):
            break
        if not line:
            continue
        try:
            a, op, b = parse(line)
            print(f"= {evaluate(a, op, b)}")
        except (ValueError, ZeroDivisionError, OverflowError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
