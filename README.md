# calculator

A simple command-line calculator — no dependencies, no framework, just Python and pytest.

```console
$ python calculator.py
Simple Calculator — supported: + - * / % **   (type 'quit' to exit)
calc> 2 ** 10
= 1024.0
calc> 7 / 2
= 3.5
calc> 1 / 0
Error: Cannot divide or take modulo by zero
```

## Why this repo exists

Replaced the old empty placeholder with the smallest possible *real* project:
working code, a test suite, and a README. Even a calculator deserves tests.

## Run it

```bash
python calculator.py
```

## Run the tests

```bash
pip install pytest
pytest -v
```

## Supported operators

| Operator | Meaning | Example |
|---|---|---|
| `+` `-` `*` | arithmetic | `2 + 3 → 5.0` |
| `/` | true division (zero-safe) | `7 / 2 → 3.5` |
| `%` | modulo (zero-safe) | `10 % 3 → 1.0` |
| `**` | power | `2 ** 10 → 1024.0` |
