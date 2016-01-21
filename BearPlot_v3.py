from __future__ import print_function
"""

TKinter documentation at http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
"""
from sys import argv
from Tkinter import *  # Python 3.4 uses tkinter where former versions used Tkinter (note cap T)
from tkMessageBox import *
import time



def main():
	filename = argv[1]		#First argument is for centroid file

	myList = [] 			#myList is used to pull each line at a time for the files
	
	
	with open(filename) as f:
		myList = f.read().splitlines()
		
	# Get TKinter ready to go
	lineCounter = 1;  # Lines of the file are numbered from 1
	main_w = {'window' : None, 'canvas' : None, 'progress': None}
	def window2(*args):
		main_w['window'] = Tk()
		main_w['canvas'] = Canvas(main_w['window'], width=int(args[0]), 
			height=int(args[1]), bg = args[2])
		main_w['canvas'].pack()
		main_w['progress'] = Label(main_w['canvas'], text = str(lineCounter))
		main_w['progress'].place( width= 30, x=int(args[0]) - 30 , y = int(args[1]) - 15 )
	
	def line (*args ):
		main_w['canvas'].create_line(int(args[0]), int(args[1]), 
			int(args[2]), int(args[3]))
	
	def lineDotted (*args):
		main_w['canvas'].create_line(int(args[0]), int(args[1]), 
			int(args[2]), int(args[3]), dash = (3,5))
	
	def lineSolid (*args):
		main_w['canvas'].create_line(int(args[0]), int(args[1]), 
			int(args[2]), int(args[3]), width = 2)
			
	def rectangle(*args):
		main_w['canvas'].create_rectangle(int(args[0]), int(args[1]), 
			int(args[2]), int(args[3]), fill=args[4])
	
	def text (*args):
		print(args)
		tempText = args[0]
		main_w['canvas'].create_text(int(args[0]), int(args[1]), 
			text=' '.join(args[2:]))
	
	def sleep (*args):
		time.sleep(float(args[0]))
	
	def oval (*args):
		main_w['canvas'].create_oval(int(args[0]), int(args[1]), 
			int(args[2]), int(args[3]))
	
	def comment():
		pass

	df = {'window' : window2, 'line' : line, 'linesolid' : lineSolid, 'linedotted': lineDotted, 'rectangle' : rectangle, 'oval' : oval, 'sleep': sleep, 'text': text, 'comment': comment}
	
	for thisLine in myList:
		
		# How to split the file line on space or TAB?
		# TBD Yikes:  split(" \t")   does not split as expected on spaces
		# How to split the file line on space or TAB?
		args = thisLine.split(" ")   # Split the file line on space or TAB
		
		# Is it helpful to have a standard case?
		# Change every token to uppercase. This accommodates input in lower or uppercase.
		#args = [e.upper() for e in args]
		if main_w['progress']:
			main_w['progress'].config(text = str(lineCounter))
		try:
			if args[0].lower() == 'comment':
				pass
			else:
				print("OK")
				df[args[0].lower()](*args[1:])
		except:
			ignore = askyesno(title ="Error", message = 'Invalid \'' + str(args[0]) + '\''  + ' command at line ' + str(lineCounter) + ". Abort?")
			if ignore:
				break
		main_w['canvas'].update()
		# TBD maybe display the line number in progress in bottom corner
		lineCounter = lineCounter + 1
		
	f.close()
	
	showinfo(title = "Continue", message="Press any key to continue")
	try:
		input= raw_input
	except NameError:
		pass
	main_w['window'].quit()
	# I don't know what this does but the script won't run without it.
	#main_w['window'].mainloop()
	
if __name__ == '__main__':
	main()
