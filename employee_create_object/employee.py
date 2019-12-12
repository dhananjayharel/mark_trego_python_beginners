class Employee:
	'Base class for our Employees'
	
	#Class Data Attributes
	first_name = 'Jaddian'
	last_name = 'Forte'
	age = '29'
	uid = '321'
	
def main():
	print('First name:', Employee.first_name)
	print('Last name:', Employee.last_name)
	print('Age:', Employee.age)
	print('User id:', Employee.uid)

main()
