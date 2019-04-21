deposit_money = []
withdrawal_money = []
total_balance = 0

print("*** Welcome to the Daily Bank ***")
print("Your Initial Account Balance =\t" + str(total_balance))
option = ""
while True:
	if option == "" or option == "choose":
		option = (input("Please choose the option to continue:\n0:\tQuit\n1:\tDeposit\n2:\tWithdrawal\n"))

	if option == "0" or option == "Quit" or option == "quit":
		print("Thank You, Have A Good Day.")
		break

	elif option == "1" or option == "Deposit" or option == "deposit":
		amount_deposit = float(input("Enter the amount you want to deposit:\t"))
		if amount_deposit < 10:
			print("\nPlease Enter the amount greater than 10")
		else:
			deposit_money.append(amount_deposit)
			total_balance += amount_deposit
			print()
			print("Your Current Account Balance:\t$" + str(total_balance))

			answer = input("Do you want to continue or choose another option?\n0\tcontinue\n1\tchoose another option")
			if answer == "0" or answer == "continue" or answer == "Continue":
				option = "1"
				continue
			else:
				option = "choose"

	elif option == "2" or option == "Withdrawal":
		print("-" * 50)
		print("\nYour Account Balance: $" + str(total_balance))
		amount_withdrawal = float(input("Enter the amount you want to withdraw:\t"))

		if amount_withdrawal > total_balance or total_balance < 10.00:
			print("\nInsufficient Funds.")
			print("\nYour Account Balance: $"+str(total_balance))
			option = "choose"
		elif amount_withdrawal < 10:
			print("Please enter the amount greater than 10.")
			continue
		else:
			withdrawal_money.append(amount_withdrawal)
			total_balance -= amount_withdrawal
			print()
			print("Your Current Account Balance:\t$" + str(total_balance))

			answer = input("Do you want to continue or choose another option?\n0\tcontinue\n1\tchoose another option")
			if answer == "0" or answer == "continue" or answer == "Continue":
				option = "2"
				continue
			else:
				option = "choose"
	else:
		print("Please Select the Appropriate Option.")
		continue
