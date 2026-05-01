from pathlib import Path

OUTPUT_DIR = Path("src")
OUTPUT_FILE = OUTPUT_DIR / "generated_calculator.py"

CODE = '''def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
'''

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(CODE, encoding="utf-8")
    print(f"Generated code written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
