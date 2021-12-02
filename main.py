from tkinter import *
import random

root = Tk()
root.title("Password Generator")
root.geometry("400x400")

label= Label(root)

array_3d =[[[1,2,3,4,5,6],["!","$","%","^","&","*","-","+","_","="], ["A","B","C","D","E","F","G","H"], ["i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"], ["16 1 19 19", "23 15 17 4"]]]
print(array_3d[0][2][3])

def myfunction():
    random_no_1 = random.randint(0,5)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,7)
    random_no_4 = random.randint(0,8)
    random_no_5 = random.randint(0,2)
    letter1 =str(array_3d[0][0][random_no_1])
    letter2 =str(array_3d[0][1][random_no_2])
    letter3 =str(array_3d[0][2][random_no_3])
    letter4 =str(array_3d[0][3][random_no_4])
    LETTER5 = str(array_3d[0][4][random_no_5])
    
    label["text"] = letter1 + " " + letter2 + " " + letter3 + " " + letter4 + " " + LETTER5
    
btn = Button(root, text="NEW PASS", command=myfunction)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label.place(relx = 0.5, rely =0.6, anchor = CENTER)
root.mainloop()