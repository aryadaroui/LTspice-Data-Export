import os

INTRO = "LTspice Data Exporter by Arya Daroui\nDrag and drop LTspice data .txt file to export to .tsv or just enter \'h\' for help"
HELP_SCREEN = "HELP SCREEN flag for .CSV file and flag for scientific notation"

def ReplaceSubstring(start, end, original, replacement):
	# Replaces a substring of the original string with a new string at given indices.
	# start: index of first element to be replaced
	# end: index of last element to be replaced
	# original: string with substring to be replaced
	# replacement: replacement string
	return original[:start] + replacement + original[end + 1:]

def Update(text):
	os.system('clear')
	print(text)

def ClearConsole():
	os.system('clear')

def Main():
	print(INTRO)

	# command = input("file: ")
	command = "/Users/aryadaroui/Desktop/High\ pass\ amp.txt" # FOR DEBUG

	ClearConsole()
	if command == "h":
		print(HELP_SCREEN)
	else:
		inFilePath = command.rstrip()	#removes whitespace
		del command
		inFilePath = inFilePath.rstrip('/')	#removes extra / at end
		inFilePath = inFilePath.replace('\ ', ' ')	#removes extra escape character prefix. could probably also use raw string
	
	ClearConsole();
	inFile = open(inFilePath, encoding = 'cp1252')
	text = inFile.read()
	text = text.replace('(', '')
	
	text = text.replace(')', '')
	text = text.replace(',', '\t')

	indexFound = text.find('\n')
	if text.find('dB') > 0:
		text = text.replace('dB', '')
		text = text.replace('°', '')
		text = ReplaceSubstring(0, indexFound - 1, text, "Frequency (Hz)\tGain (dB)\tPhase (°)")
		# text = "Frequency (Hz)\tGain (dB)\tPhase (°)" + text[indexFound:]
	else:
		text = ReplaceSubstring(0, indexFound - 1, text, "Frequency (Hz)\tReal\tImaginary")
		# text = "Frequency (Hz)\tReal\tImaginary"
	
	while text.find('e+') > 0:
		indexFound = text.find('e+')
		endIndex = indexFound + 4
		startIndex = indexFound - 16
		replacement = text[startIndex : endIndex + 1]
		pad = str(15 - len(str(int(float(replacement)))))
		buff = "{0:." + pad + "f}"
		replacement = buff.format(float(replacement))
		text = ReplaceSubstring(startIndex, endIndex, text, replacement)
		Update(text)

	while text.find('e-') > 0:
		indexFound = text.find('e-')
		endIndex = indexFound + 4
		startIndex = indexFound - 16
		pad = str(15 - len(str(int(float(text[startIndex:endIndex+1])))))
		buff = "{0:." + pad + "f}"
		replacement = buff.format(float(text[startIndex:endIndex+1]))
		text = ReplaceSubstring(startIndex, endIndex, text, replacement)
		Update(text)

	outFilePath = inFilePath.replace('txt', 'tsv')

	outFile = open(outFilePath, "w")
	outFile.write(text)

Main()