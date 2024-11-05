from tkinter import *
import tkinter.font as font
import random

root=Tk()
root.geometry("1000x500")
root.title("Rock, paper and scissor!!")
root.config(bg="white")

player_score=0
computer_score=0
options=[("rock",0),("paper",1),("scissor",2)]

def aiwins():
    global computer_score,player_score
    computer_score+=1
    winner_label.config(text="🤖 Won!!!!!")
    playerscore_label.config(text="🧑 score: "+str(player_score))
    aiscore_label.config(text="🤖 score: "+str(computer_score))

def playerwins():
    global computer_score,player_score
    player_score+=1
    winner_label.config(text="🧑 Won!!!!!")
    playerscore_label.config(text="🧑 score: "+str(player_score))
    aiscore_label.config(text="🤖 score: "+str(computer_score))

def tie():
    global computer_score,player_score
    winner_label.config(text="Tie!!!!!")
    playerscore_label.config(text="🧑 score: "+str(player_score))
    aiscore_label.config(text="🤖 score: "+str(computer_score))


def get_computer_choice():
    return random.choice(options)

def get_player_choice(player_input):
    global computer_score,player_score
    computer_input=get_computer_choice()
    playerchoice_label.config(text="🧑 choice: "+player_input[0])
    aichoice_label.config(text="🤖 choice: "+computer_input[0])

    if(player_input==computer_input):
        tie()

    if(player_input[1]==0):
        if(computer_input[1]==1):
            aiwins()
        elif(computer_input[1]==2):
            playerwins()

    elif(player_input[1]==1):
        if(computer_input[1]==0):
            playerwins()
        elif(computer_input[1]==2):
            aiwins()

    elif(player_input[1]==2):
        if(computer_input[1]==0):
            aiwins()
        elif(computer_input[1]==1):
            playerwins()
    

app_font=font.Font(size=16)

rps_label=Label(text="Rock, paper and scissors!!",font=font.Font(size=40),fg="black",bg="white")
rps_label.pack()

winner_label=Label(text="Let's start the game...",font=font.Font(size=25),fg="green",bg="white")
winner_label.pack()

input_frame=Frame(root,background="white")
input_frame.pack()

playopt_label=Label(input_frame,text="🧑 options: ",font=app_font,fg="gray",bg="white")
playopt_label.grid(row=0,column=0,pady=8)

rock_button=Button(input_frame,text="🪨",width=15,bd=0,bg="pink",pady=5,command=lambda:get_player_choice(options[0]))
rock_button.grid(row=1,column=1,padx=8,pady=5)

paper_button=Button(input_frame,text="📄",width=15,bd=0,bg="pink",pady=5,command=lambda:get_player_choice(options[1]))
paper_button.grid(row=1,column=2,padx=8,pady=5)

scissor_button=Button(input_frame,text="✂️",width=15,bd=0,bg="pink",pady=5,command=lambda:get_player_choice(options[2]))
scissor_button.grid(row=1,column=3,padx=8,pady=5)

score_label=Label(input_frame,text="Score: ",font=app_font,fg="gray",bg="white")
score_label.grid(row=2,column=0,pady=8)

playerchoice_label=Label(input_frame,text="🧑 choice: ---",font=app_font,fg="gray",bg="white")
playerchoice_label.grid(row=3,column=1,pady=8)

aichoice_label=Label(input_frame,text="🤖 choice: ---",font=app_font,fg="gray",bg="white")
aichoice_label.grid(row=4,column=1,pady=8)

playerscore_label=Label(input_frame,text="🧑 score: ---",font=app_font,fg="gray",bg="white")
playerscore_label.grid(row=3,column=2,pady=8)

aiscore_label=Label(input_frame,text="🤖 score: ---",font=app_font,fg="gray",bg="white")
aiscore_label.grid(row=4,column=2,pady=8)



root.mainloop()
