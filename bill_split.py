# Simple calculator for splitting the bill
print("Bill Split Calculator")

bill_amount = float(input())
tip_percent = float(input())
num_people = int(input())
total_price = bill_amount * (1 + (tip_percent / 100))
amount_per_person = total_price / num_people

print(f"Total (including tip): ${total_price}")
print(f"Each person pays: ${amount_per_person}")