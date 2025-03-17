def calculate_bill_split():
    """Calculate and display bill split with tip among multiple people"""
    print("=== Bill Split Calculator ===")

    # Using a try-except block for error handling
    try:
        # Get user inputs with clear prompts
        bill_amount = float(input("Enter the bill amount ($): "))
        tip_percent = (float(input("Enter tip percentage (%): ")))
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

        # Display results with proper formatting (2 decimal places for money)
        print("\n--- Bill Breakdown ---")
        print(f"Bill Amount: ${bill_amount:.2f}")
        print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
        print(f"Total (with tip): ${total_price:.2f}")
        print(f"Amount per person: ${amount_per_person:.2f} ({num_people} people)")

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
