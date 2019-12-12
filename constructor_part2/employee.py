class Employee:
	'Base class for our Employees'
	
	def __init__(self, myFirstName, myLastName, myUID):
		self.first_name = myFirstName
		self.last_name = myLastName
		self.uid = myUID
		
	def show_employee_details(self):
		print('First name:', self.first_name)
		print('Last name:', self.last_name)
		print('User id:', self.uid)
		
	
def main():
	#create new object
	employee = Employee('John','Wilson','622')
	#show details
	employee.show_employee_details()

main()
