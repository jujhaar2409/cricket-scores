import numpy as np
from tkinter import *
from PIL import ImageTk, Image
import os
import pandas as pd
import matplotlib.pyplot as plt

window = Tk()

window.title('Cricket Scores')

window.configure(background = 'white')

def click3():

	def click4(entered_text):				
	
		if entered_text.lower() == 'vk':
				
				myfile = open(r"players/virat_kohli.txt",'r')
				x = myfile.read()
				playerpage = Toplevel()
				w = Label(playerpage, text=x,justify=LEFT)
				w.pack()
				w.mainloop()
				myfile.close()                        
				
		elif entered_text.lower() == 'msd':
				
				myfile=open(r"players/MS_Dhoni.txt",'r')
				x=myfile.read()
				playerpage=Toplevel()
				w = Label(playerpage, text=x,justify=LEFT)
				w.pack()
				w.mainloop()
				myfile.close()
				
		elif entered_text.lower() =='sd':
				
				myfile=open(r"players/Shikhar_Dhawan.txt",'r')
				x=myfile.read()
				playerpage=Toplevel()
				w = Label(playerpage, text=x,justify=LEFT)
				w.pack()
				w.mainloop()
				myfile.close()

		elif entered_text.lower() =='gg':
				
				myfile=open(r"players/Gautam_Gambhir.txt",'r')
				x=myfile.read()
				playerpage=Toplevel()
				w = Label(playerpage, text=x,justify=LEFT)
				w.pack()
				w.mainloop()
				myfile.close()

		elif entered_text.lower() =='kd':
				
				myfile=open(r"players/Kapil_Dev.txt",'r')
				x=myfile.read()
				playerpage=Toplevel()
				w = Label(playerpage, text=x,justify=LEFT)
				w.pack()
				w.mainloop()
				myfile.close()

		elif entered_text.lower() =='st':
				
				myfile=open(r"players/Sachin_Tendulkar.txt",'r')
				x=myfile.read()
				playerpage=Toplevel()
				w = Label(playerpage, text=x,justify=LEFT)
				w.pack()
				w.mainloop()
				myfile.close()
	
	new_window = Toplevel()

	Label (new_window, text = 'Choose a player to view his details', fg = 'black',bg = 'white', font = 'ariel' ).grid(row = 0 , column = 1, sticky= N )

	vk = ImageTk.PhotoImage(Image.open("images/vk.jpg").resize((175, 175), Image.ANTIALIAS))

	msd = ImageTk.PhotoImage(Image.open("images/msd.jpg").resize((175, 175), Image.ANTIALIAS))

	sd = ImageTk.PhotoImage(Image.open("images/sd.jpg").resize((175, 175), Image.ANTIALIAS))

	gg = ImageTk.PhotoImage(Image.open("images/gg.jpg").resize((175, 175), Image.ANTIALIAS))

	kd = ImageTk.PhotoImage(Image.open("images/kd.jpg").resize((175, 175), Image.ANTIALIAS))

	st = ImageTk.PhotoImage(Image.open("images/st.jpg").resize((175, 175), Image.ANTIALIAS))

	Button(new_window, width = 225, height = 225 , text = 'Virat Kohli', image = vk,compound = TOP ,command = lambda: click4('vk')).grid (row = 3, column  = 0)

	Button(new_window, width = 225, height = 225 , text = 'MS Dhoni', image = msd,compound = TOP ,command = lambda: click4('msd')).grid (row = 3, column  = 1)

	Button(new_window, width = 225, height = 225 , text = 'Shikhar Dhawan', image = sd,compound = TOP  ,command = lambda: click4('sd')).grid (row = 3, column  = 2)
	
	Button(new_window, width = 225, height = 225 , text = 'Gautam Gambhir', image = gg,compound = TOP , command = lambda: click4('gg')).grid (row = 4, column  = 0)

	Button(new_window, width = 225, height = 225 , text = 'Kapil Dev', image = kd,compound = TOP  ,command = lambda: click4('kd')).grid (row = 4, column  = 1)

	Button(new_window, width = 225, height = 225 , text = 'Sachin Tendulkar', image=st,compound = TOP ,command = lambda: click4('st')).grid (row = 4, column  = 2)
	
	new_window.mainloop()

def click1():#sort button

	dir = os.path.dirname(__file__)

	def teams_sort(data):
		
		data.sort_values("POINTS", axis = 0, ascending = False, inplace = True, na_position ='last')
		return (data.to_string(index=False))

	def runs_sort(data):
		
		data.sort_values("RUNS", axis = 0, ascending = False, inplace = True, na_position ='last')
		return (data.to_string(index=False))

	def wickets_sort(data):
		
		data.sort_values("WICKETS", axis = 0, ascending = False, inplace = True, na_position ='last')
		return (data.to_string(index=False))

	entered_text = variable.get()
	
	output.delete(0.0, END)
	
	s1 = ''

	# Import the excel file and call it xls_file
	runs_ = pd.ExcelFile(os.path.join(dir, 'excel_files/runs.xlsx'))
	
	wickets_ = pd.ExcelFile(os.path.join(dir,'excel_files/wickets.xlsx'))
	
	teams_ = pd.ExcelFile(os.path.join(dir,'excel_files/teams.xlsx'))

	# Load the excel_file's Sheet1 as a dataframe
	teams = teams_.parse('Sheet1')
	
	wickets = wickets_.parse('Sheet1')
	
	runs = runs_.parse('Sheet1')

	if entered_text == 'runs':
		
		s1 += runs_sort(runs) + '\n'

		s1 += 'TO GO TO MAIN MENU ENTER MENU'


	elif entered_text == 'teams':
		
		s1 += teams_sort(teams) + '\n'
		s1 +='TO GO TO MAIN MENU ENTER MENU'

	elif entered_text == 'wickets':
		
		s1 += wickets_sort(wickets) + '\n'
		s1 +='TO GO TO MAIN MENU ENTER MENU'

	else:
		s1 += 'Please select one of the below options:\n-teams\n-runs\n-wickets\n\nPLEASE CHOOSE SOMETHING ELSE'

	output.insert(END,s1)

def click2():#graph
	
	def graph_(x, y, xl, yl):
		# # libraries

		# # Fake dataset
		height = list(int(i) for i in y)
		bars = x
		y_pos = np.arange(len(bars))

		# # Create bars and choose color
		plt.bar(y_pos, height)

		# # Add title and axis names
		# plt.title(entered_text)

		# # Limits for the Y axis
		#plt.ylim(0, max(height)*6/5)

		# # Create names
		plt.xticks(y_pos, bars)
		plt.xlabel(xl)
		plt.ylabel(yl)
		# # Show graphic
		plt.show()

	def teams_sort(data):
		
		data.sort_values("POINTS", axis=0, ascending=False,
						 inplace=True, na_position='last')
		return (data.to_string(index=False))

	def runs_sort(data):
		
		data.sort_values("RUNS", axis = 0, ascending = False, inplace = True, na_position ='last')
		return (data.to_string(index=False))

	def wickets_sort(data):
		
		data.sort_values("WICKETS", axis = 0, ascending = False, inplace = True, na_position ='last')
		return (data.to_string(index=False))

	y = []
	x = []

	dir = dir = os.path.dirname(__file__)
	
	runs_ = pd.ExcelFile(os.path.join(dir, 'runs.xlsx'))
	
	wickets_ = pd.ExcelFile(os.path.join(dir,'wickets.xlsx'))
	
	teams_ = pd.ExcelFile(os.path.join(dir,'teams.xlsx'))

	# Load the excel_file's Sheet1 as a dataframe
	teams = teams_.parse('Sheet1')
	
	wickets = wickets_.parse('Sheet1')
	
	runs = runs_.parse('Sheet1')

	entered_text = variable.get()

	if entered_text == 'runs':
		
		data = runs_sort(runs)
		data = data.split('\n')

		for i in range(1,len(data)):
			
			l = data[i].split()
			x.append(l[0])
			y.append(l[1])

		graph_(x, y, 'Players', 'Runs')

	elif entered_text == 'wickets':
		
		data = wickets_sort(wickets)
		data = data.split('\n')

		for i in range(1,len(data)):
			
			l = data[i].split()
			x.append(l[0])
			y.append(l[1])

		graph_(x, y, 'Players', 'Wickets')

	elif entered_text == 'teams':
		
		data = teams_sort(teams)
		data = data.split('\n')

		for i in range(1,len(data)):
			
			l = data[i].split()
			x.append(l[0])
			y.append(l[1])

		graph_(x,y,'Teams','Points')

OPTIONS=['teams', 'runs' , 'wickets']


variable = StringVar(window)
variable.set('teams/wickets/runs')


Label (window, text = 'Welcome to the Cricket score board' ,fg = 'black',bg = 'white', font = 'ariel' ).grid(row = 0 , column = 0, columnspan =5 , sticky= N )

#text = Entry(window , width = 20 , bg = 'light gray')

#text.grid(row = 2, column = 1,columnspan = 3, sticky = N)

Button(window , text = 'TABLE',width = 20 , command = click1). grid (row = 2, column  = 2, sticky = E)

Button(window , text = 'GRAPH',width = 20 , command = click2). grid (row = 2, column  = 3, sticky = W)

Button(window , text = 'PLAYER DETAILS',width = 20 , command = click3). grid (row = 3, column  = 2, sticky = S)

output = Text(window, width = 57, height = 12 , wrap = WORD , background = 'white')

output.grid ( row = 5, column = 1, columnspan = 3, sticky = N)

output.config(font = ('consolas','11'), background = 'white', insertontime = 0)

w = OptionMenu(window, variable, *OPTIONS)

w.config(width = 18)

w.grid(row=2,column=1,sticky=W )

s1 = '-Select one of the options from the drop down list\n\n-Click "TABLE" to see the points table on the basis of field chosen\n\n-Click GRAPH to see a pictorial representation of the feild  chosen\n\n-To veiw the details of player click PLAYER DETAILS'

output.insert(END, s1)

window.mainloop()
