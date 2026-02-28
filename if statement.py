def check_weather(temperature):
	if temperature > 30:
		print("It's a really hot day!")
	elif temperature > 25:
		print("It's a hot day!")
	else:
		print("It's a nice day")

temperature = 31
check_weather(temperature)
