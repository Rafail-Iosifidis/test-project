from datetime import datetime


def main() -> None:
    print("Hello, Codex!")
    print(f"Current date and time: {datetime.now():%Y-%m-%d %H:%M:%S}")

    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    print(f"Sum: {first + second}")


if __name__ == "__main__":
    main()
