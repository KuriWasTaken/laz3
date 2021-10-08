import random
import decimal

def laz3Encode(msg, Key):
	if not len(Key) > 3:
		return "Key is to short!"
	count = 0
	finalstring = ""
	dividers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	resources = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_", "*", "'", "^", "~", "!", '"', "'", "=", ",", ":", ";", ")", "(", "{", "}"]
	lCount = 0
	newKey = 0
	for i in enumerate(Key):
		for v in resources:
			if i[1] == v:
				newKey = newKey + lCount *256
				lCount = 0
			lCount += 1
	Key = newKey
	for i in enumerate(msg):
		for v in resources:
			if i[1] == v:
				finalstring = finalstring + random.choice(dividers) + str(count / 256 * Key)
				count = 0			
			count += 1
		count = 0	
	return finalstring + random.choice(dividers)

def laz3Decode(msg, Key):
	if not len(Key) > 3:
		return "Key is to short!"
	finalstring = ""
	dividers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	resources = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_", "*", "'", "^", "~", "!", '"', "'", "=", ",", ":", ";", ")", "(", "{", "}"]
	lCount = 0
	newKey = 0
	for i in enumerate(Key):
		for v in resources:
			if i[1] == v:
				newKey = newKey + lCount *256
				lCount = 0
			lCount += 1
	Key = newKey
	encodedChars = []
	singleChar = ""

	def checkArray(TBL, Wanted):
		for i in TBL:
			if i == Wanted:
				return True
		return False

	def dropzeros(number):
		mynum = decimal.Decimal(number).normalize()
		return mynum.__trunc__() if not mynum % 1 else float(mynum)

	for i in enumerate(msg):
		if checkArray(dividers, i[1]):
			if singleChar != "":
				encodedChars.append(singleChar)
				singleChar = ""
		else:
			singleChar = singleChar + i[1]
	for i in encodedChars:
		cChar = int(float(i) * 256 / Key)
		finalstring = finalstring + resources[int(dropzeros(cChar))]
	
	return finalstring
