class MyClass:
	'Base class for our Employees'
	
	def __init__(self):
		print('Creating new object...')
		
	def __del__(self):
		print('Deleting used object...')
		
	
def main():
	object1 = MyClass()
	object2 = MyClass()
	object3 = MyClass()
	
	print('\n\n')
	del(object1)
	del(object2)
	del(object3)
	

main()
