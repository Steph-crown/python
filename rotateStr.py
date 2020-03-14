def rotateStr(string):
	string = string.lower()
	rotatedStr = ""
	for i in string:
		rotatedStr += chr(ord("z") - (ord(i) - ord("a")))
	return rotatedStr
st = input ("Input string\t")
print (rotateStr(st))