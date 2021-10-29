units = int(input('Enter Number of units conusmed : '))
fixedCharge = 125
if 0 < units <= 100:
    totalBill: float = units * 3.7
elif 200 >= units > 100 :
    totalBill: float = units * 7.4
elif 500 >= units < 200 :
    totalBill: float = units * 10
else:
    totalBill: float = units * 15

totalBill=totalBill+fixedCharge
print("Your bill is :: " , totalBill)
