import tkinter as tk
import random
from tkinter import messagebox as tmsg
comp=0
player=0

def user_choi(choice):
    global player,comp
    comp_choi = computers_choice()
    winner= det_winner(choice,comp_choi)
    round_res=f"Your choice is : {choice}\nComputer's choice is : {comp_choi}\n"
    if winner=='User':
        round_res+="It's your win"
        player+=1
    elif winner=='Computer':
        round_res+="It's your lose"
        comp+=1
    else:
        round_res+="It's a tie"
    tmsg.showinfo('Result', round_res)
    scr_label.config(text=f"Your score : {player}\nComputer's score : {comp}")
    play_again=tmsg.askyesno('Play again?', "Do you want to play again?")
    if play_again==False:
        r.destroy()

    

def computers_choice():
    comp_choice=random.choice(['Rock','Paper','Scissor'])
    return comp_choice

def det_winner(choice,comp_choi):
    if comp_choi==choice:
        return 'tie'
    elif (comp_choi=='Rock' and choice=='Scissor') or (comp_choi=='Scissor' and choice=='Paper') or (comp_choi=='Paper' and choice=='Rock'):
       return 'Computer'
    else:
       return 'User'

    
def main():
    global scr_label, comp, player, r
    r=tk.Tk()
    r.configure(bg='#282c34')
    r.geometry('500x300')
    r.title('Rock Paper Scissor')

    tk.Label(r, bg='#61dafb', text='Rock, Paper, Scissor', font='Arial 20 bold').pack(side=tk.TOP, fill=tk.X)

    f=tk.Frame(r, bg='#282c34')
    f.pack(side=tk.TOP, pady=20)
    tk.Label(f, bg='#282c34', text='Choose any one of them', font='Arial 14 bold').pack(pady=10)
    tk.Button(f, text="ROCK",font='helvetica 12 bold', fg="white", bg="#ff5733", command=lambda: user_choi('Rock')).pack(side=tk.LEFT, pady=10, padx=10)
    tk.Button(f, text="PAPER", font='helvetica 12 bold', fg="white", bg="#33cfff", command=lambda: user_choi('Paper')).pack(side=tk.LEFT, pady=10, padx=10)
    tk.Button(f, text="SCISSOR", font='helvetica 12 bold', fg="white", bg="#b833ff", command=lambda: user_choi('Scissor')).pack(side=tk.LEFT, pady=10, padx=10)

    scr_label = tk.Label(r, text=f"Your score : {player}\nComputer's score : {comp}", font='helvetica 14 italic', bg='#282c34', fg='#61dafb')
    scr_label.pack(side=tk.BOTTOM, pady=20)

    
    r.mainloop()

if __name__=='__main__':
    main()