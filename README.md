# Bill Splitting Calculator

A simple yet powerful Python tool to split restaurant bills among friends, including tip calculations. Perfect for quick and accurate bill splitting without the hassle!

---

## Features
- Calculates the total bill with tip included
- Splits the amount evenly among a specified number of people
- **Optional rounding of per-person amounts (up to nearest dollar or cent)**
- Handles invalid inputs with clear error messages
- Offers a replay option to calculate multiple bills in one session
- Clean, formatted output for easy reading

---

## How to Run
1. **Prerequisites**: Ensure you have Python 3 installed (`python3 --version` to check).
2. **Download**: Clone or download this repository to your local machine.
3. **Run the Script**: Open a terminal in the project folder and execute:
   ```bash
   python3 bill_split.py
   
(Note: Use `python` instead of `python3` if that’s how Python 3 is configured on your system.)
   
## Example Output
Here’s what you’ll see when you run the program:

>=== Bill Split Calculator ===<br>
Enter the bill amount ($): 50<br>
Enter tip percentage (%): 15<br>
Enter number of people to split among: 4<br><br>
>--- Bill Breakdown ---<br>
Bill Amount: \$50.00<br>
Tip (15.0%): \$7.50<br>
Total (with tip): \$57.50<br>
Amount per person: 14.38 (4 people)<br><br>
>Calculate another bill? (yes/no):

If you enter invalid input (e.g., "abc" or a negative number), it gracefully handles it:
>Error: Please enter valid numeric values!

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bill-splitting-calculator.git
2. Navigate to the directory:
   ```bash
   cd bill-splitting-calculator
3. Run the script as described above.

## Contributing
Feel free to fork this project, submit pull requests, or open issues for bugs and feature suggestions! Ideas for improvement:

- Add rounding options for per-person amounts
- Support uneven bill splitting
- Export results to a file

Built with ❤️ by Jacob
