# Bill Splitting Calculator

A powerful Python tool to split restaurant bills among friends with customizable options. Calculate tips, assign amounts to named individuals, and save results effortlessly!

---

## Features
Latest change is in **bold**
- Calculates the total bill with tip included
- Supports **even splitting** or **uneven splitting with custom amounts for some, remainder split evenly**
- Tracks amounts owed by **named individuals**
- Optional rounding of per-person amounts (no rounding, nearest cent, or up to nearest dollar)
- **Adjusts the last person’s amount to ensure the total matches the bill, with adjustment noted only when necessary**
- Saves bill breakdowns to a text file
- Reprompts for input on errors instead of crashing, making it typo-friendly
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
   
## Example Usage
Here’s what you’ll see when you run the program:

> === Bill Split Calculator ===<br>
Enter the bill amount (\$): 50<br>
Enter tip percentage (%): 23<br>
Enter number of people to split among: 3<br>
Enter name for person 1: Jacob<br>
Enter name for person 2: Jay<br>
Enter name for person 3: Nick<br>
Even split (e) or uneven split with custom amounts (u)? u<br>
How many people pay a custom amount? (0 to cancel uneven split): 1<br>
Remaining to allocate: \$61.50<br>
Enter name of person 1 paying custom amount: Jay<br>
Enter amount for Jay (\$): 25<br>
> 
> Round the per-person amounts?<br>
1: No rounding (default)<br>
2: Round to nearest cent (2 decimal places)<br>
3: Round up to nearest dollar<br>
Enter choice (1-3): 1<br>
> 
> --- Bill Breakdown ---<br>
Bill Amount: \$50.00<br>
Tip (23.0%): \$11.50<br>
Total (with tip): \$61.50<br>
Jay: \$25.00<br>
Jacob: \$18.25<br>
Nick: \$18.25<br>
> 
> Save breakdown to file? (yes/no): yes<br>
Enter filename (e.g., bill.txt): dominos.txt<br>
Saved to dominos.txt<br>
> 
> Calculate another bill? (yes/no): no<br>
Thanks for using Bill Split Calculator!<br>

And here’s an example where adjustment is needed if you enter invalid input (e.g., "abc" or a negative number):
> Enter the bill amount (\$): asd<br>
Please enter a valid number!<br>
Enter the bill amount (\$):<br>

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

- Add a GUI interface
- Allow editing of previous entries
- Support multiple currency formats
- Include tax calculations by location

Built with ❤️ by Jacob