B = input("Buying price of product:\n")
print(f"Buying Price is:{B}")
S = input("Selling price of product is:\n")
print(f"Selling Price is:{S}")
profitloss = int(S) - int(B)
if profitloss > 0:
    print("Your profit is:")
    print(f"Your profit is:{profitloss}")
elif profitloss < 0:
    print("Your loss is:")
    print(f"Your loss is:{profitloss}")
else :
    print("No loss No Profit")
    print(f"No profit No Loss:{profitloss}")