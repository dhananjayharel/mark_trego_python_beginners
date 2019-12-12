class Employee:
	'Base class for our Employees'
	
	def __init__(self):
		self.first_name = 'Jaddian'
		self.last_name = 'Forte'
		self.uid = '855'

	def get_first_name(self):
		return self.first_name


	def get_last_name(self):
		return self.last_name

	def get_uid(self):
		return self.uid

	
def main():
	employee_01 = Employee()
	print('First name:', employee_01.get_first_name())
	print('Last name:', employee_01.get_last_name())
	print('User id:', employee_01.get_uid())

main()
