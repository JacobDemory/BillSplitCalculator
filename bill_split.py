import math

def calculate_bill_split():
    """Calculate and display bill split with tip among multiple people."""
    print("=== Bill Split Calculator ===")

    # Using a try-except block for error handling
    try:
        # Get user inputs with clear prompts
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
        amount_per_person = total_price / num_people

        # Ask about rounding preference
        print("\nRound the per-person amount?")
        print("1: No rounding (default)")
        print("2: Round to nearest cent (2 decimal places)")
        print("3: Round up to nearest dollar")
        rounding_choice = input("Enter choice (1-3): ").strip()

        # Apply rounding based on user choice
        if rounding_choice == "3":
            amount_per_person = math.ceil(amount_per_person)  # Round up to nearest dollar
            rounding_note = " (rounded up to nearest dollar)"
        elif rounding_choice == "2":
            amount_per_person = round(amount_per_person, 2)  # Nearest cent
            rounding_note = " (rounded to nearest cent)"
        else:
            amount_per_person = amount_per_person  # No rounding (keep as is)
            rounding_note = ""

        # Display results with proper formatting
        print("\n--- Bill Breakdown ---")
        print(f"Bill Amount: ${bill_amount:.2f}")
        print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
        print(f"Total (with tip): ${total_price:.2f}")
        print(f"Amount per person: ${amount_per_person:.2f}{rounding_note} ({num_people} people)")

    except ValueError as e:
        # Handle invalid inputs gracefully
        if str(e).startswith("Bill") or str(e).startswith("Number"):
            print(f"Error: {e}")
        else:
            print("Error: Please enter valid numeric values!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the calculator and offer replay option."""
    while True:
        calculate_bill_split()

        # Ask if user wants to calculate another bill
        replay = input("\nCalculate another bill? (yes/no): ").lower().strip()
        if replay != "yes":
            print("Thanks for using Bill Split Calculator!")
            break

if __name__ == "__main__":
    main()