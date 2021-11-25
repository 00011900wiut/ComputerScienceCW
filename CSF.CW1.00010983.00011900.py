import re
#creating regular expression
numberRegEx = re.compile(r'\d{2}/\d{2}/\d{4}')

#function to check if MC claim is accepted or not
def isValid():
	isValidReason = input("Do you have a valid reason(Yes(y)/No(n)): ")
	if isValidReason == "y":
		mcAcceptedCheck = input("MC accepted?(Yes(y)/No(n)): ")
		return mcAcceptedCheck == "y"
	else:
		return False

#if month is 31 days or not
months31 = [1, 3, 5, 7, 8, 10, 12]

isNumber = True
isGoing = True
isFinished = False

#main loop
while isGoing:
#checks if the given number is correct or not
	while isNumber:
		cwDeadline = input("Please enter deadline for CW submission(day/month/year): ")
		cwSubmission = input("Please enter the day you submitted your CW(day/month/year): ")
		if numberRegEx.match(cwDeadline) and numberRegEx.match(cwSubmission):
			isNumber = False
		else:
			print("Please enter valid number (Ex: 08/03/2020)")
#splitting day, month and year by using "/" sign
	cwDeadlineDate = cwDeadline.split("/")
	cwSubmissionDate = cwSubmission.split("/")
#converting to the integer
	deadlineDay = int(cwDeadlineDate[0])
	deadlineMonth = int(cwDeadlineDate[1])
	submissionDay = int(cwSubmissionDate[0])
	submissionMonth = int(cwSubmissionDate[1])

#checks the month (For example:
# if the deadline was in the 31st Jan and submission was in 1st Feb the result will be "You submitted your work within a day")
	if submissionMonth - deadlineMonth > 0 and isFinished == False:
		if submissionMonth - deadlineMonth == 1 and isFinished == False:
			if deadlineDay - submissionDay > 25 and isFinished == False:
				if deadlineMonth in months31 and isFinished == False:
					if deadlineDay - submissionDay == 30 and isFinished == False:
						print("You submitted your work within a day")
						if isValid():
							print("You will get full mark")
							isFinished = True
						else:
							print("Minus 10 mark from overall mark, but not below 40")
							isFinished = True
					else:
						print(f"You submitted your work within {submissionDay + 1} days")
						if isValid():
							print("You will get full mark")
							isFinished = True
						else:
							print("Mark = 0")
							isFinished = True

				else:
					if deadlineDay - submissionDay == 29 and isFinished == False:
						print("You submitted your work within a day")
						if isValid():
							print("You will get full mark")
							isFinished = True
						else:
							print("Minus 10 mark from overall mark, but not below 40")
							isFinished = True
					else:
						print(f"You submitted your work within {submissionDay + 1} days")
						if isValid():
							print("You will get full mark")
							isFinished = True
						else:
							print("Mark = 0")
							isFinished = True

			print("You submitted your work after one month")
		else:
			print(f"You submitted your work after {submissionMonth - deadlineMonth} months")
		if not isFinished:
			if isValid():
				print("You will get full mark")
				isFinished = True
			else:
				print("Mark = 0")
				isFinished = True
#compares the days
	if submissionDay - deadlineDay < 0 and submissionMonth - deadlineMonth == 0 and isFinished == False:
		print("You will get full mark")

	if submissionDay - deadlineDay == 1 and isFinished == False:
		print("You submitted your work within a day")
		if isValid():
			print("You will get full mark")
			isFinished = True
		else:
			print("Minus 10 mark from overall mark, but not below 40")
			isFinished = True
	if submissionDay - deadlineDay > 1 and submissionMonth - deadlineMonth == 0 and isFinished == False:
		print(f"You submitted your work within {submissionDay - deadlineDay} days")
		if isValid():
			print("You will get full mark")
			isFinished = True
		else:
			print("Mark = 0")
			isFinished = True
#reruns the code of the users input was "y" if the opposite it stops
	wannaContinue = input("Would you like to restart (Yes(y)/No(n))? ")

	if wannaContinue == "n":
		isGoing = False
	else:
		isGoing = True
		isNumber = True
		isFinished = False




