#genrating a alphanumeric code on registration

import random
import string


def randomalpha(length):
	letter = string.ascii_letters + string.digits
	code = ''.join(random.choice(letter) for i in range(length))
	return code


def generate_id(length):
	num = string.digits
	id_num = ''.join(random.choice(num) for i in range(length))
	return id_num


def register():
	info = {}
	refbal = 0
	option: str = ''

	while True:
		if option == '':
			option = input("\nPlease choose the option\n1. Sign In\n2. Register\n3. Quit\n").strip().lower()

		if option == "quit" or option == "3":
			print("\n**********THANK YOU*************")
			break
		elif option == "sign in" or option == "signin" or option == "1":
			identity = input("Enter your id number: ")

			if identity in info:
				password = input("Enter your password: ").strip()
				if password == info[identity]["password"]:

					print('\nid', identity)
					for i in info[identity]:
						print(i, info[identity][i])

					print("\nYour Referral Balance is:$", info[identity]['referralBalance'])
					option = '3'
				else:
					print('Invalid Password')
					continue

			else:
				print("Wrong Id or Password. Try Again")
				print("\nYou Need to Register First.")
				print()
				option = '2'

		elif option == 'register' or option == "2":
			name = input("\nEnter your name:\t").strip()
			password = input("Enter your password:\t").strip()

			if len(password) < 8:
				print("Password should contain Minimum 8 characters.")
				option = '2'

			else:
				curr_id = generate_id(4)
				info.update({curr_id: {'name': name, 'password': password, 'referralBalance': refbal}})
				#
				# answer = input("Put Referral Code:")
				# if answer == 'yes':
				referral_code = input("Enter Referral Code:\t")
				if referral_code != curr_id:
					if referral_code in info:
						info[referral_code]['referralBalance'] += 10
						info[curr_id]['referralBalance'] += 5

				elif referral_code == curr_id:
					print("Not a Valid Referral Code.")
					continue
				else:
					print("Not a Valid Referral Code.")
					continue
					#print(info[referral_code]['ref'])
				print(info)
				print("*" * 500)

				answer = input(
					"Do you want to continue or choose another option?\n0\tcontinue\n1\tchoose another option").strip().lower()
				if answer == "0" or answer == "continue" or answer == "Continue":
					option = "2"
					continue
				else:
					option = ''
		else:
			print("Please Choose The Appropriate Option.")
			option = ''


register()
