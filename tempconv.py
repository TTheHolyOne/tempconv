'''
github.com/ttheholyone
TTheHolyOne#1642
Temp Convert
'''


print('Hello there! If you are a Celcius or a Fahrenheit user I will convert it for you!\n\n\n')
input('Press any key to proceed...')
while True:
	char = input('Press Q to quit or enter C to convert Celcius into Fahrenheit or enter F to convert Fahrenheit into Celcius!\n')

	if char.lower() == 'q':
		break
	if char.lower() == 'c':
		c = input('Please enter the Celcius of a number you want to convert: \n')
		first = int(c) * 2
		second = first + 30
		print(f'Your estimated temperature in degrees Fahrenheit is °F {second}!')
	elif char.lower() == 'f':
		f = input('Please enter the Fahrenheit of a number you want to convert: \n')
		first = int(f) - 30
		second = first / 2
		print(f'Your estimated temperature in degrees Celcius is °C {second}!')
print('Shutting down...')
