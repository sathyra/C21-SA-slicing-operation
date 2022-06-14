import numpy as np
from tkinter import *
root=Tk()
root.geometry("600x400")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#Defining the slicing function
def sl_ar():
        i = int(input1.get())
        j = int(input2.get())
        #Write a code to add the slcing operation
        label.config(text=newarr1)
        
#display the array numbers
Message(root, text= arr,bg='light blue', font = 50).pack()

#display the the heading as slicing ration
Label(root, text = "Enter Slicing ratio: ", font = 30).pack()

#Write a code to Get the start point for slice


#Display the colon(:) in between start and end point
Message(root, text= ":", bg='light blue', font = 100).pack()

#Write a code to Get the end point for slice

#Write a code to call the slice function when button is clicked

#output is displayed using the label
label = Label(root,bg='light blue', font = 50)
label.pack()

root.mainloop()