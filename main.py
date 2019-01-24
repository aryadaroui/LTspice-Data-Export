import os

INTRO = "LTspice Data Exporter by Arya Daroui\nDrag and drop LTspice data .txt file to export to .tsv or just enter \'h\' for help"
HELP_SCREEN = "add the following switches after file to modify output.\n\n-c\t.csv\n-s\tkeep scientific notation\n"

def ReplaceSubstring(start, end, original, replacement):
	# Replaces a substring of the original string with a new string at given indices. TODO proper error handling
	# start: index of first element to be replaced
	# end: index of last element to be replaced
	# original: string with substring to be replaced
	# replacement: replacement string
	return original[:start] + replacement + original[end + 1:]

def	SetNumberWidth(width, value):
	# Returns a string of a float with of certain length or width by adjusting its precision. TODO proper error handling for when width is too small
	# width: desired output length
	# value: value to be formatted
	value = float(value) # converts sci notation to float, which removes trailing zeros
	pad = str(width - 1 - len(str(int(value)))) # determines needed precision to maintain width
	style = "{0:." + pad + "f}"
	outputText = style.format(value)
	return outputText

def Update(text):
	Clear()
	print(text)

def Clear():
	os.system('clear')

def Main():
	csvFlag = False
	sciFlag = False

	command = "h" # to make it a do-while loop
	while command == "h":
		print(INTRO)
		command = input("file: ")

		Clear()
		if command == "h":
			print(HELP_SCREEN)
		else:
			switch = command[command.find('.txt') + 4:]
			command = command[:command.find('.txt')+4]
			if switch.find(" -c") >= 0:
				csvFlag = True
			if switch.find(" -s") >= 0:
				sciFlag = True

			inFilePath = command.rstrip()	# removes whitespace
			inFilePath = inFilePath.rstrip('/')	# removes extra / at end
			inFilePath = inFilePath.replace(r'\ ', ' ')	# removes extra escape character prefix
			print(inFilePath)
			print(switch)
	del command

	
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
	
	if not sciFlag:
		while text.find('e+') > 0 or text.find('e-') > 0:
			indexFound = text.find('e+')
			if indexFound < 0:
				indexFound = text.find('e-')
			endIndex = indexFound + 4
			startIndex = indexFound - 16

			text = ReplaceSubstring(startIndex, endIndex, text, SetNumberWidth(16, text[startIndex : endIndex + 1]))

	if csvFlag:
		text = text.replace('\t', ',')
		outFileType = 'csv'
	else:
		outFileType = 'tsv'

	Update(text)

	outFilePath = inFilePath.replace('txt', outFileType)
	print(outFilePath)
	outFile = open(outFilePath, "w")
	outFile.write(text)

Main()