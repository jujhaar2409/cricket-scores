from tkinter import *
import os
import pandas as pd
import matplotlib.pyplot as plt

window = Tk()
window.title('Cricket Scores')
window.configure(background = 'white')

# name_sort()
# runs_sort()
# wickets_sort()

def click1():
	# teams_ = ['TEAM', 'POINTS', 'WON', 'LOST']
	# runs_ = ['PLAYERS', 'RUNS', 'MATCHES', 'AVERAGE']
	# wickets_ = ['PLAYERS', 'WICKETS', 'MATCHES', 'WICKETS/MATCH']
	# players = ['Virat', 'Rohit', 'Dhoni', 'Dhawan']
	# scores = [100, 150, 128, 40]
	# wickets = [5, 1, 4, 1]
	# wins = [1, 2, 1, 0]
	# teams = ['RCB', 'MI', 'CSK', 'SRH']
	# matches_played = [2, 3, 2, 1]

	dir = os.path.dirname(__file__)
	# path= os.path.join(dir,'data.txt')

	# with open(path, 'r') as f:
	# 	d = f.readlines()
	# d = d[1].split('|')

	# teams_ = d[0].split(',')
	# runs_ = d[1].split(',')
	# wickets_ = d[2].split(',')
	# players = d[3].split(',')
	# scores = list( int(i) for i in d[4].split(',') )
	# wickets = list( int(i) for i in d[5].split(',') )
	# wins = list( int(i) for i in d[6].split(',') )
	# teams = d[7].split(',')
	# matches_played = list(int(i) for i in d[8].split(','))

	# loses = []
	# points = []

	# for i in range(len(wins)):
	# 	loses.append(matches_played[i] - wins[i])
	# 	points.append(2*wins[i])

	def create_list(data):
		return

	def teams_sort(data):
		data.sort_values("POINTS", axis = 0, ascending = False, inplace = True, na_position ='last')
		return (data.to_string(index=False))
	def runs_sort(data):
		data.sort_values("RUNS", axis = 0, ascending = False, inplace = True, na_position ='last')
		return (data.to_string(index=False))
	def wickets_sort(data):
		data.sort_values("WICKETS", axis = 0, ascending = False, inplace = True, na_position ='last')
		return (data.to_string(index=False))

	entered_text = text.get()
	output.delete(0.0, END)
	s1 = ''

	# Import the excel file and call it xls_file
	runs_ = pd.ExcelFile(os.path.join(dir, 'runs.xlsx'))
	wickets_ = pd.ExcelFile(os.path.join(dir,'wickets.xlsx'))
	teams_ = pd.ExcelFile(os.path.join(dir,'teams.xlsx'))

	# Load the excel_file's Sheet1 as a dataframe
	teams = teams_.parse('Sheet1')
	wickets = wickets_.parse('Sheet1')
	runs = runs_.parse('Sheet1')

	if entered_text == 'runs':
		# for i in range (len(runs_)):
		# 	s = runs_[i]
		# 	s1 += s + ( 20 - len(s) )*' '
		# s1 += '\n'

		# for i in range(len(players)):

		# 	s1 += (players[i] + ' ' * (20 - len(players[i])) + str(str(scores[i])) + ' ' * (20 - len(str(scores[i]))) +
        #   			str(matches_played[i]) + ' '*(20-len(str(matches_played[i]))) + str(scores[i]/matches_played[i]) + '\n\n' )

		s1 += runs_sort(runs) + '\n'

		s1 += 'TO GO TO MAIN MENU ENTER MENU'


	elif entered_text == 'teams':
		# for i in range(len(teams_)):
		# 	s = teams_[i]
		# 	s1 += s + ' '*(20 - len(s))
		# s1 += '\n'

		# for i in range(len(teams)):

		# 	s1 += (teams[i] + ' ' * (20 - len(teams[i])) + str(points[i]) + ' ' * (20 - len(str(points[i]))) +
        #   			str(wins[i]) + ' '*(20-len(str(wins[i]))) + str(loses[i]) + '\n\n')

		s1 += teams_sort(teams) + '\n'
		s1 +='TO GO TO MAIN MENU ENTER MENU'

	elif entered_text == 'wickets':
		# for i in range(len(wickets_)):
		# 	s = wickets_[i]
		# 	s1 += s + ' '*(20 - len(s))
		# s1 += '\n'

		# for i in range(len(players)):

		# 	s1 += (players[i] + ' ' * (20 - len(players[i])) + str(str(wickets[i])) + ' ' * (20 - len(str(wickets[i]))) +
        # 			str(matches_played[i]) + ' '*(20-len(str(matches_played[i]))) + str(wickets[i]/matches_played[i]) + '\n\n')
		s1 += wickets_sort(wickets) + '\n'
		s1 +='TO GO TO MAIN MENU ENTER MENU'

	else:
		s1 += 'Please select one of the below options:\n-teams\n-runs\n-wickets\n\nPLEASE CHOOSE SOMETHING ELSE'

	output.insert(END,s1)

# def click():
# 	players = ['Virat', 'Rohit', 'Dhoni', 'Dhawan']
# 	scores = [100, 150, 128, 40]
# 	matches_played = [2, 3, 2, 1]
# 	entered_text = text.get()
# 	if entered_text == 'runs':
# 		output.delete(0.0,END)
# 		output.insert(END, 'PLAYERS' + ' '*13 + 'RUNS' + ' '*16 + 'MATCHES'+' '* (13) + 'AVERAGE' + '\n')
# 		for i in range (len(players)):
# 			output.insert(END, players[i] + ' ' * (20 - len(players[i])) + str(str(scores[i])) + ' ' * (20 - len(str(scores[i]))) + str(
# 				matches_played[i]) + ' '*(20-len(str(matches_played[i]))) + str(scores[i]/matches_played[i]) + '\n')
# 	else:
# 		Label(window, text=' Please give some other input ', fg='black', bg='white', font='ariel').grid(row=8 , column=3, sticky=W)

Label (window, text = 'Welcome to the Cricket score board' ,fg = 'black',bg = 'white', font = 'ariel' ).grid(row = 1 , column = 6 , sticky= N )
text = Entry(window , width = 20 , bg = 'light gray')
text.grid(row = 3, column = 6, sticky = N)
Button(window , text = 'ENTER',width = 20 , command = click1). grid (row = 4, column  = 6, sticky = N)
Label (window, text = 'SCORES' ,fg = 'black',bg = 'white', font = 'ariel' ).grid(row = 6 , column = 6 , sticky= N )

output = Text(window, width = 60 , height = 10 , wrap = WORD , background = 'white')
output.grid ( row = 7 , column = 6 , columnspan = 2 , sticky = W )
s1 = 'Please select one of the below options:\n-teams\n-runs\n-wickets'
output.insert(END, s1)

window.mainloop()
