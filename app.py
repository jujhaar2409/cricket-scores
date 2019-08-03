from tkinter import *

window = Tk()
window.title('Cricket Scores')
window.configure(background = 'white')

def click1():
	teams_ = ['TEAM', 'POINTS', 'WON', 'LOST']
	runs_ = ['PLAYERS', 'RUNS', 'MATCHES', 'AVERAGE']
	wickets_ = ['PLAYERS', 'WICKETS', 'MATCHES', 'WICKETS/MATCH']
	players = ['Virat', 'Rohit', 'Dhoni', 'Dhawan']
	scores = [100, 150, 128, 40]
	wickets = [5, 1, 4, 1]
	wins = [1, 2, 1, 0]
	teams = ['RCB', 'MI', 'CSK', 'SRH']
	matches_played = [2, 3, 2, 1]
	loses = []
	points = []
	for i in range(len(wins)):
		loses.append(matches_played[i] - wins[i])
		points.append(2*wins[i])

	entered_text = text.get()
	output.delete(0.0, END)
	s1 = ''

	if entered_text == 'runs':
		for i in range (len(runs_)):
			s = runs_[i]
			s1 += s + ( 20 - len(s) )*' '
		s1 += '\n'
		for i in range(len(players)):
			s1 += (players[i] + ' ' * (20 - len(players[i])) + str(str(scores[i])) + ' ' * (20 - len(str(scores[i]))) + str(matches_played[i]
                                                                                                                   ) + ' '*(20-len(str(matches_played[i]))) + str(scores[i]/matches_played[i]) + '\n\n' )
		s1 += 'TO GO TO MAIN MENU ENTER MENU'
	elif entered_text == 'teams':
		for i in range(len(teams_)):
			s = teams_[i]
			s1 += s + ' '*(20 - len(s))
		s1 += '\n'
		for i in range(len(teams)):
			s1 += (teams[i] + ' ' * (20 - len(teams[i])) + str(points[i]) + ' ' * (20 - len(str(points[i]))) + str(wins[i]) + ' '*(20-len(str(wins[i]))) + str(loses[i]) + '\n\n')
		s1 +='TO GO TO MAIN MENU ENTER MENU'
	elif entered_text == 'wickets':
		for i in range(len(wickets_)):
			s = wickets_[i]
			s1 += s + ' '*(20 - len(s))
		s1 += '\n'
		for i in range(len(players)):
			s1 += (players[i] + ' ' * (20 - len(players[i])) + str(str(wickets[i])) + ' ' * (20 - len(str(wickets[i]))) +
			       str(matches_played[i]) + ' '*(20-len(str(matches_played[i]))) + str(wickets[i]/matches_played[i]) + '\n\n')
		s1 +='TO GO TO MAIN MENU ENTER MENU'
	else:
		s1 += 'Please select one of the below options:\n-teams\n-runs\n-wickets\n\nPLEASE CHOOSE SOMETHING ELSE'

	output.insert(END,s1)

'''
def click():
	players = ['Virat', 'Rohit', 'Dhoni', 'Dhawan']
	scores = [100, 150, 128, 40]
	matches_played = [2, 3, 2, 1]
	entered_text = text.get()
	if entered_text == 'runs':
		output.delete(0.0,END)
		output.insert(END, 'PLAYERS' + ' '*13 + 'RUNS' + ' '*16 + 'MATCHES'+' '* (13) + 'AVERAGE' + '\n')
		for i in range (len(players)):
			output.insert(END, players[i] + ' ' * (20 - len(players[i])) + str(str(scores[i])) + ' ' * (20 - len(str(scores[i]))) + str(
				matches_played[i]) + ' '*(20-len(str(matches_played[i]))) + str(scores[i]/matches_played[i]) + '\n')
	else:
		Label(window, text=' Please give some other input ', fg='black', bg='white', font='ariel').grid(row=8 , column=3, sticky=W)
'''



Label (window, text = 'Welcome to the Cricket score board' ,fg = 'black',bg = 'white', font = 'ariel' ).grid(row = 1 , column = 6 , sticky= N )
text = Entry(window , width = 20 , bg = 'light gray')
text.grid(row = 3, column = 6, sticky = N)
Button(window , text = 'ENTER',width = 20 , command = click1). grid (row = 4, column  = 6, sticky = N)
Label (window, text = 'SCORES' ,fg = 'black',bg = 'white', font = 'ariel' ).grid(row = 6 , column = 6 , sticky= N )

output = Text(window, width = 90 , height = 10 , wrap = WORD , background = 'white')
output.grid ( row = 7 , column = 6 , columnspan = 2 , sticky = W )
s1 = 'Please select one of the below options:\n-teams\n-runs\n-wickets'
output.insert(END, s1)

window.mainloop()
