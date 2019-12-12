class Employee:
	'Base class for our Employees'
	
	#Class Data Attributes
	first_name = 'Jaddian'
	last_name = 'Forte'
	age = '29'
	uid = '321'

def get_fist_name(self):
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
