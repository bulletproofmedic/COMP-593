#-----------------------------------------------------
#   Lab 1, Pyfiglet - COMP 593
#
#   Description:
#       Displays some trippy text.
#
#   Usage:
#       python pyfiglet.py
#
#   Parameters:
#       No CLI parameters.
#
#   History:
#   Date        Author      Description
#   2022-02-07  A. Walker   Initial Creation
#-----------------------------------------------------

from pyfiglet import Figlet
from random import randint

#Instantiate a Figlet Object
figlet = Figlet()

#Set font variables/constants
fonts = figlet.getFonts()
num_fonts = len(fonts)
NUM_FONT_OPTIONS = 5

#Initiate loop
play = True
while play == True:
	#Randomize fonts for each iteration of the loop
	font_index = []
	font_1 = fonts[randint(0,num_fonts - 1)]
	font_2 = fonts[randint(0,num_fonts - 1)]
	font_3 = fonts[randint(0,num_fonts - 1)]
	font_4 = fonts[randint(0,num_fonts - 1)]
	font_5 = fonts[randint(0,num_fonts - 1)]
	font_index.append(font_1)
	font_index.append(font_2)
	font_index.append(font_3)
	font_index.append(font_4)
	font_index.append(font_5)

	#Display font selection
	print("There are", num_fonts, "different fonts available for use. Here are",
	NUM_FONT_OPTIONS, "random fonts to choose from.")
	print("1. ", font_1)
	print("2. ", font_2)
	print("3. ", font_3)
	print("4. ", font_4)
	print("5. ", font_5)

	#Prompt user to select a font
	selectedFont = input("Select a font (1-5): ")
	if selectedFont.isnumeric() == False:
		print("Do you understand the concept of numbers. Try a number this time.")
		continue
	elif int(selectedFont) > 5 or int(selectedFont) < 1:
		print("You've chosen an invalid number - let's start over.")
		continue
	for num in range(1, NUM_FONT_OPTIONS +1):
		if int(selectedFont) == num:
			figlet.setFont(font = font_index[num - 1])
			#print("You've selected", font_ + num)
			print(figlet.renderText(input("Enter some text: ")))
	again = input("Do you want to play again? ")
	if again.lower() == "yes":
		continue
	else:
		break
