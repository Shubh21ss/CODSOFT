def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b
def modulus(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a % b
def power(a, b): return a ** b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠ Please enter a valid number.")

def main():
    print("\n  ====================================")
    print("       CODSOFT - CALCULATOR APP      ")
    print("  ====================================")

    operations = {
        "1": ("+", "Addition",        add),
        "2": ("-", "Subtraction",     subtract),
        "3": ("*", "Multiplication",  multiply),
        "4": ("/", "Division",        divide),
        "5": ("%", "Modulus",         modulus),
        "6": ("^", "Power",           power),
    }

    while True:
        print("\n  SELECT OPERATION:")
        for key, (sym, name, _) in operations.items():
            print(f"  {key}. {sym}  {name}")
        print("  7. Exit")

        choice = input("\n  Choose an option (1-7): ").strip()

        if choice == "7":
            print("\n  Goodbye! Happy calculating! 👋\n")
            break
        elif choice in operations:
            sym, name, func = operations[choice]
            print(f"\n  --- {name} ---")
            a = get_number("  Enter first number : ")
            b = get_number("  Enter second number: ")
            result = func(a, b)

            if isinstance(result, str):
                print(f"\n  ⚠  {result}")
            else:
                # Show as int if result is whole number
                display = int(result) if isinstance(result, float) and result.is_integer() else result
                print(f"\n  ✔  {a} {sym} {b} = {display}")
        else:
            print("  Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()
