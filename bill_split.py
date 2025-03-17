# Simple calculator for splitting the bill
print("Bill Split Calculator")

bill_amount = float(input())
tip_percent = float(input())

print(bill_amount * (1 + (tip_percent / 100)))