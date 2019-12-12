class Employee:
	'Base class for our Employees'
	
	def __init__(self):
		self.first_name = 'N/A'
		self.last_name = 'N/A'
		self.uid = 'N/A'



	
def main():
	employee_01 = Employee()
	print('First name:', employee_01.first_name)
	print('Last name:', employee_01.last_name)
	print('User id:', employee_01.uid)
	print()

	employee_01.first_name = 'Bobby'
	employee_01.last_name = 'Jones'
	employee_01.uid = '552'
	print('New Values')
	print('First name:', employee_01.first_name)
	print('Last name:', employee_01.last_name)
	print('User id:', employee_01.uid)	

main()
