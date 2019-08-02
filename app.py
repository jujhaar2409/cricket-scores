from tkinter import *

window = Tk()
window.title('Cricket Scores')
window.configure(background = 'white')

players = [ 'Virat' , 'Rohit' , 'Dhoni' , 'Dhawan' ]
scores = [100 , 150 , 128 , 40]

matches_played = [2 , 3 , 2 , 1]

def click():
    players = ['Virat', 'Rohit', 'Dhoni', 'Dhawan']
    scores = [100, 150, 128, 40]
    matches_played = [2, 3, 2, 1]
    entered_text = text.get()
    if entered_text == 'runs':
        output.delete(0.0,END)
        output.insert(END, 'PLAYERS' + ' '*13 + 'RUNS' + ' '*16 + 'MATCHES\n')
        for i in range (len(players)):
            output.insert(END, players[i] + ' ' * (20 - len(players[i]))+ str(str(scores[i])) + ' ' * (20 - len(str(scores[i])))+ str(matches_played[i]) + '\n')
    else:
        Label(window, text=' Please give some other input ', fg='black', bg='white', font='ariel').grid(row=8 , column=3, sticky=W)

Label (window, text = 'Welcome to the Cricket score board' ,fg = 'black',bg = 'white', font = 'ariel' ).grid(row = 1 , column = 6 , sticky= N )
text = Entry(window , width = 20 , bg = 'light gray')
text.grid(row = 3, column = 6, sticky = N)
Button(window , text = 'ENTER',width = 20 , command = click). grid (row = 4, column  = 6, sticky = N)
Label (window, text = 'SCORES' ,fg = 'black',bg = 'white', font = 'ariel' ).grid(row = 6 , column = 6 , sticky= N )

output = Text(window, width = 75 , height = 10 , wrap = WORD , background = 'white')
output.grid ( row = 7 , column = 6 , columnspan = 2 , sticky = W )

window.mainloop()
