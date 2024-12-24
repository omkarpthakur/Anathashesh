import anant

while True:
	text = input("\033[1;38;5;214mananthshesh > \033[0m")
	if text.strip() == "": continue
	result, error = anant.run('<stdin>', text)

	if error:
		print("\033[1;31m" + error.as_string() + "\033[0m")
	elif result:
		if len(result.elements) == 1:
			print("\033[1;38;5;33m" + repr(result.elements[0])+ "\033[0m")
		else:
			print("\033[1;38;5;33m" + repr(result) + "\033[0m")