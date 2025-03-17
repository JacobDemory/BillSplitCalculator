import math

def calculate_bill_split():
    """Calculate and display bill split with tip among multiple people."""
    print("=== Bill Split Calculator ===")

    try:
        # Get basic inputs
        bill_amount = float(input("Enter the bill amount ($): "))
        tip_percent = float(input("Enter tip percentage (%): "))
        num_people = int(input("Enter number of people to split among: "))

        # Validate inputs
        if bill_amount < 0 or tip_percent < 0:
            raise ValueError("Bill amount and tip percentage must be positive!")
        if num_people <= 0:
            raise ValueError("Number of people must be at least 1!")

        # Calculations
        tip_amount = bill_amount * (tip_percent / 100)
        total_price = bill_amount + tip_amount

        # Ask about split type
        split_type = input("Even split (e) or uneven split (u)? ").lower().strip()

        # Collect names and amounts
        people = []
        if split_type == "u":
            remaining = total_price
            for i in range(num_people):
                name = input(f"Enter name for person {i + 1}: ").strip()
                if i == num_people - 1:  # Last person gets the remainder
                    amount = remaining
                else:
                    amount = float(input(f"Enter amount for {name} ($): "))
                    if amount < 0 or amount > remaining:
                        raise ValueError(f"Amount must be between 0 and ${remaining:.2f}!")
                    remaining -= amount
                people.append((name, amount))
            if remaining > 0.01:  # Check if there's unallocated money
                raise ValueError(f"${remaining:.2f} was not allocated!")
        else:  # Even split
            amount_per_person = total_price / num_people
            for i in range(num_people):
                name = input(f"Enter name for person {i + 1}: ").strip()
                people.append((name, amount_per_person))

        # Rounding option
        print("\nRound the per-person amounts?")
        print("1: No rounding (default)")
        print("2: Round to nearest cent (2 decimal places)")
        print("3: Round up to nearest dollar")
        rounding_choice = input("Enter choice (1-3): ").strip()

        # Apply rounding and build breakdown
        breakdown = []
        for name, amount in people:
            if rounding_choice == "3":
                rounded_amount = math.ceil(amount)
                note = " (rounded up to nearest dollar)"
            elif rounding_choice == "2":
                rounded_amount = round(amount, 2)
                note = " (rounded to nearest cent)"
            else:
                rounded_amount = amount
                note = ""
            breakdown.append((name, rounded_amount, note))

        # Display results
        print("\n--- Bill Breakdown ---")
        print(f"Bill Amount: ${bill_amount:.2f}")
        print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
        print(f"Total (with tip): ${total_price:.2f}")
        for name, amount, note in breakdown:
            print(f"{name}: ${amount:.2f}{note}")

    except ValueError as e:
        if (str(e).startswith("Bill") or str(e).startswith("Number") or
                str(e).startswith("Amount")):
            print(f"Error: {e}")
        else:
            print("Error: Please enter valid numeric values!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the calculator and offer replay option."""
    while True:
        calculate_bill_split()
        replay = input("\nCalculate another bill? (yes/no): ").lower().strip()
        if replay != "yes":
            print("Thanks for using Bill Split Calculator!")
            break

if __name__ == "__main__":
    main()