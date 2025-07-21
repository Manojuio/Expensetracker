filename = "expenses.txt"

print("📊 Expense Tracker")
print("1. Add Expense")
print("2. View Total")
choice = input("Choose option: ")

if choice == '1':
    amount = float(input("Enter amount spent: "))
    reason = input("Reason (e.g. food, recharge): ")
    with open(filename, 'a') as f:
        f.write(f"{amount},{reason}\n")
    print("✅ Expense saved.")
elif choice == '2':
    total = 0
    try:
        with open(filename, 'r') as f:
            print("\nYour Expenses:")
            for line in f:
                amount, reason = line.strip().split(',')
                print(f"- ₹{amount} for {reason}")
                total += float(amount)
        print(f"\n💰 Total spent: ₹{total}")
    except FileNotFoundError:
        print("❌ No expenses found yet.")
else:
    print("⚠️ Invalid option.")