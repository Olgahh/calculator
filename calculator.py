
def main():
	#write your code here
	first_number = input("Enter the first number: ")
	second_number = input("Enter the second number: ")
	operation = input("Choose the operation (+, -, /, *): ")

	if  not first_number.isdigit() or not second_number.isdigit():
		print("The numbers are not valid")
	else:
		if operation == '*':
				print("The answer is ", int(first_number)*int(second_number))
		elif operation == '+':
				print("The answer is ", int(first_number)+int(second_number))
		elif operation == '-':
				print("The answer is ", int(first_number)-int(second_number))
		elif operation =='/':
				print("The answer is ", int(first_number)/int(second_number))
		else:
			print("The operation is not valid")



	pass




if __name__ == '__main__':
	main()
