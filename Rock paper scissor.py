from tkinter import *
from PIL import Image,ImageTk
from random import randint
#main window
root=Tk()
root.title("Rock Paper Scissor")
root.configure(background="#00ffff")

#pictures
rock_img=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor.jpg"))


#insert picture
user_lable=Label(root,image=rock_img,bg="#00ffff")
comp_lable=Label(root,image=rock_img,bg="#00ffff")
comp_lable.grid(row=1,column=0)
user_lable.grid(row=1,column=8)



#indicator
user_indicater=Label(root,text="You",font=50,bg="white",fg="black")
Computer_indicater=Label(root,text="Opponent",font=50,bg="white",fg="black")
user_indicater.grid(row=0,column=8)
Computer_indicater.grid(row=0,column=0)

#messages
msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=5,column=4)

#update message
def updatemsg(x):
    msg['text']=x


choice=["rock","paper","scissor"]

#ckeak winner
def win(player,computer):
    if player==computer:
        updatemsg("Its a tie!!!")
    elif player=="rock":
        if computer=="paper":
            updatemsg("You loose")
            
        else:
            updatemsg("You win")
            
    elif player=="paper":
        if computer=="scissor":
            updatemsg("You loose")
            
        else:
            updatemsg("You win")
            
    elif player=="scissor":
        if computer=="rock":
            updatemsg("You loose")
            
        else:
            updatemsg("You win")

    else:
        pass
#update choice
def update(x):

#computer choice
    compchoice=choice[randint(0,2)]
    if compchoice=="rock":
        comp_lable.configure(image=rock_img)
    elif compchoice=="paper":
        comp_lable.configure(image=paper_img)
    else:
        comp_lable.configure(image=scissor_img)
#user choice
    if x=="rock":
        user_lable.configure(image=rock_img)
    elif x=="paper":
        user_lable.configure(image=paper_img)
    else:
        user_lable.configure(image=scissor_img)
    win(x,compchoice)
#button
rock=Button(root,width=40,height=4,text="rock",bg="#FF3E4D" , fg="white",command=lambda:update("rock"))
paper=Button(root,width=40,height=4,text="paper",bg="#FAD02E" , fg="white",command=lambda:update("paper"))
scissor=Button(root,width=40,height=4,text="Scissor",bg="#0ABDE3" , fg="white",command=lambda:update("scissor"))
rock.grid(row=2,column=0)
paper.grid(row=2,column=4)
scissor.grid(row=2,column=8)
root.mainloop()