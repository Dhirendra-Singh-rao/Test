P = int(input("Enter principal amount: "))
R = int(input("Enter rate of interest: "))
N = int(input("Enter time tenure in years: "))

simple_interest = (P * R * N) / 100
total_payable_amount = P + simple_interest
monthly_installment = N * 12
EMI = total_payable_amount / monthly_installment

print("Simple Interest:", simple_interest)
print("Total Payable Amount:", total_payable_amount)
print("EMI:", EMI)

balance = P

for i in range(1, monthly_installment + 1):
    # Recalculate monthly principal each time as remaining principal divided by remaining months
    remaining_months = monthly_installment - i + 1
    current_monthly_principal = balance / remaining_months

    print(f"{i}. Monthly Principal: {current_monthly_principal}")
    
    monthly_interest_paid = (balance * R) / (100 * 12)
    print("Monthly Interest Paid:", monthly_interest_paid)
    
    amount_paid = EMI
    print("Amount Paid:", amount_paid)
    
    balance = current_monthly_principal
    print("Balance:", balance)
