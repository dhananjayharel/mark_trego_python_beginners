class Employee:
	'Base class for our Employees'
	
	def __init__(self):
		self.first_name = 'NA'
		self.last_name = 'NA'
		self.uid = 'NA'

	def get_first_name(self):
		return self.first_name

	def get_last_name(self):
		return self.last_name

	def get_uid(self):
		return self.uid
		

	def set_first_name(self,xFirstName):
		self.first_name = xFirstName

	def set_last_name(self,xLastName):
		self.last_name = xLastName

	def set_uid(self,xUID):
		self.uid = xUID
	
def main():
	employee_01 = Employee()
	
	print('First name:', employee_01.get_first_name())
	print('Last name:', employee_01.get_last_name())
	print('User id:', employee_01.get_uid())
	employee_01.set_first_name('John')
	employee_01.set_last_name('Williams')
	employee_01.set_uid('631')	
	print()
	print('New Values:')
	print('First name:', employee_01.get_first_name())
	print('Last name:', employee_01.get_last_name())
	print('User id:', employee_01.get_uid())	
	

main()
