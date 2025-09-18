


print("Welcome to the Bill Splitter App!\n")

while True:
  
    total_bill = float(input("\n Enter total bill amount: "))

    people = int(input("\nEnter number of people: "))

    percent = int(input("\nEnter tip percentage (0/5/10/15/20): "))

    amount=(percent/100)*total_bill

    total_with_tip= total_bill + amount

    per_person = total_with_tip / people

    print(f"\nTip Amount: ₹{amount:.2f}")

    print(f"\n Total Bill (with Tip): ₹{total_with_tip:.2f}")

    print(f"\n Each person should pay: ₹{per_person:.2f}\n")

    again = input("Would you like to calculate another bill? (y/n): ").lower()

    if again != 'y':

        print("\n Thank you for using the Bill Splitter App!")

        break


