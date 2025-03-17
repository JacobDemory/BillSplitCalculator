import math

def get_float_input(prompt, min_value=None, max_value=None):
    """Helper function to get valid float input with optional min/max values."""
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a value of at least {min_value}!")
                continue
            if max_value is not None and value > max_value:
                print(f"Please enter a value no more than {max_value:.2f}!")
                continue
            return value
        except ValueError:
            print("Please enter a valid number!")

def get_int_input(prompt, min_value=None, max_value=None):
    """Helper function to get valid integer input with optional min/max values."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a value of at least {min_value}!")
                continue
            if max_value is not None and value > max_value:
                print(f"Please enter a value no more than {max_value}!")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer!")

def calculate_bill_split():
    """Calculate and display bill split with tip, supporting names, practical uneven splits, and file export."""
    print("=== Bill Split Calculator ===")

    # Get basic inputs with reprompting
    bill_amount = get_float_input("Enter the bill amount ($): ", min_value=0)
    tip_percent = get_float_input("Enter tip percentage (%): ", min_value=0)
    num_people = get_int_input("Enter number of people to split among: ", min_value=1)

    # Calculations
    tip_amount = bill_amount * (tip_percent / 100)
    total_price = bill_amount + tip_amount

    # Collect all names first
    people = []
    for i in range(num_people):
        while True:
            name = input(f"Enter name for person {i+1}: ").strip()
            if not name:
                print("Name cannot be empty!")
            elif name in people:
                print("Name must be unique!")
            else:
                people.append(name)
                break

    # Ask about split type
    while True:
        split_type = input("Even split (e) or uneven split with custom amounts (u)? ").lower().strip()
        if split_type in ["e", "u"]:
            break
        print("Please enter 'e' or 'u'!")

    # Handle split logic
    breakdown = []
    remaining = total_price
    if split_type == "u":
        num_custom = get_int_input("How many people pay a custom amount? (0 to cancel uneven split): ",
                                 min_value=0, max_value=num_people-1)
        if num_custom == 0:
            split_type = "e"  # Fall back to even split
        else:
            # Assign custom amounts
            custom_people = []
            for i in range(num_custom):
                print(f"Remaining to allocate: ${remaining:.2f}")
                while True:
                    name = input(f"Enter name of person {i+1} paying custom amount: ").strip()
                    if name not in people:
                        print(f"{name} is not in the group! Choose from: {', '.join(people)}")
                    elif name in custom_people:
                        print(f"{name} already has a custom amount!")
                    else:
                        break
                amount = get_float_input(f"Enter amount for {name} ($): ", min_value=0, max_value=remaining)
                custom_people.append(name)
                breakdown.append((name, amount, ""))
                remaining -= amount
            # Split remainder evenly among others
            remaining_people = [p for p in people if p not in custom_people]
            if remaining_people:
                amount_per_remaining = remaining / len(remaining_people)
                for name in remaining_people:
                    breakdown.append((name, amount_per_remaining, ""))
    if split_type == "e":  # Even split
        amount_per_person = total_price / num_people
        breakdown = [(name, amount_per_person, "") for name in people]

    # Rounding option
    while True:
        print("\nRound the per-person amounts?")
        print("1: No rounding (default)")
        print("2: Round to nearest cent (2 decimal places)")
        print("3: Round up to nearest dollar")
        rounding_choice = input("Enter choice (1-3): ").strip()
        if rounding_choice in ["1", "2", "3", ""]:
            break
        print("Please enter 1, 2, 3, or press Enter for default!")

    # Apply rounding
    rounded_breakdown = []
    for name, amount, _ in breakdown:
        if rounding_choice == "3":
            rounded_amount = math.ceil(amount)
            note = " (rounded up to nearest dollar)"
        elif rounding_choice == "2":
            rounded_amount = round(amount, 2)
            note = " (rounded to nearest cent)"
        else:
            rounded_amount = amount
            note = ""
        rounded_breakdown.append((name, rounded_amount, note))

    # Display results
    print("\n--- Bill Breakdown ---")
    print(f"Bill Amount: ${bill_amount:.2f}")
    print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
    print(f"Total (with tip): ${total_price:.2f}")
    total_assigned = sum(amount for _, amount, _ in rounded_breakdown)
    for name, amount, note in rounded_breakdown:
        print(f"{name}: ${amount:.2f}{note}")
    if abs(total_assigned - total_price) > 0.01:  # Allow small float errors
        print(f"Warning: Total assigned (${total_assigned:.2f}) does not match total (${total_price:.2f})!")

    # Save to file option
    while True:
        save = input("\nSave breakdown to file? (yes/no): ").lower().strip()
        if save in ["yes", "no"]:
            break
        print("Please enter 'yes' or 'no'!")
    if save == "yes":
        while True:
            filename = input("Enter filename (e.g., bill.txt): ").strip()
            if filename:
                break
            print("Filename cannot be empty!")
        with open(filename, "w") as f:
            f.write("Bill Breakdown\n")
            f.write(f"Bill Amount: ${bill_amount:.2f}\n")
            f.write(f"Tip ({tip_percent}%): ${tip_amount:.2f}\n")
            f.write(f"Total (with tip): ${total_price:.2f}\n")
            for name, amount, note in rounded_breakdown:
                f.write(f"{name}: ${amount:.2f}{note}\n")
            if abs(total_assigned - total_price) > 0.01:
                f.write(f"Warning: Total assigned (${total_assigned:.2f}) does not match total (${total_price:.2f})!\n")
        print(f"Saved to {filename}")

def main():
    """Main function to run the calculator and offer replay option."""
    while True:
        calculate_bill_split()
        while True:
            replay = input("\nCalculate another bill? (yes/no): ").lower().strip()
            if replay in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'!")
        if replay != "yes":
            print("Thanks for using Bill Split Calculator!")
            break

if __name__ == "__main__":
    main()