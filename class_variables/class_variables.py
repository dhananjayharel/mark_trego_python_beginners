class Employee:
	'Base class for Employee'
	
	#Class Variables
	
    employeeCount	= 0
	payRate = 10

	
def __init__(self):
	self.firstName = 'N/A'
	self.lastName = 'N/A'
	self.uid = 'N/A'


print('Employee Count:', Employee.employeeCount)

