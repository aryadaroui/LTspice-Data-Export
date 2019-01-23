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
	Clear()
	print(text)

def Clear():
	os.system('clear')

def Main():
	print(INTRO)

	# command = input("file: ")
	command = r"/Users/aryadaroui/Desktop/High\ pass\ amp.txt" # FOR DEBUG

	Clear()
	if command == "h":
		print(HELP_SCREEN)
	else:
		inFilePath = command.rstrip()	# removes whitespace
		del command
		inFilePath = inFilePath.rstrip('/')	# removes extra / at end
		inFilePath = inFilePath.replace(r'\ ', ' ')	# removes extra escape character prefix
	
	Clear()
	inFile = open(inFilePath, encoding = 'cp1252') # 8-bit encoding
	text = inFile.read()
	text = text.replace('(', '')
	text = text.replace(')', '')
	text = text.replace(',', '\t')

	indexFound = text.find('\n')
	# TO DO make robust function to handle datatype, i.e. voltage current
	if text.find('dB') > 0:
		text = text.replace('dB', '')
		text = text.replace('°', '')
		text = ReplaceSubstring(0, indexFound - 1, text, "Frequency (Hz)\tGain (dB)\tPhase (°)")
	else:
		text = ReplaceSubstring(0, indexFound - 1, text, "Frequency (Hz)\tReal\tImaginary")
	
	while text.find('e+') > 0 or text.find('e-') > 0:
		indexFound = text.find('e+')
		if indexFound < 0:
			indexFound = text.find('e-')
		endIndex = indexFound + 4
		startIndex = indexFound - 16
		replacement = text[startIndex : endIndex + 1]
		pad = str(15 - len(str(int(float(replacement))))) # converts sci notation to float, which removes trailing
		style = "{0:." + pad + "f}"
		replacement = style.format(float(replacement))

		text = ReplaceSubstring(startIndex, endIndex, text, replacement)
		Update(text)

	outFilePath = inFilePath.replace('txt', 'tsv')
	outFile = open(outFilePath, "w")
	outFile.write(text)

Main()