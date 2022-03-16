# importing the packages

import tkinter as tk

from tkinter import *

from tkinter import messagebox

# creating the root window

root = tk.Tk()

root.minsize(700, 500)  # setting the size of the

# main window

root.title("Dog n Suds.")  # title of the window

# image code:
hotdog = PhotoImage(file='hotdog.gif') # keep the pictures with file, also remove this random note and the other on zoom
hotdog.zoom(320)
#showin the hotdog
hotdog_label = Label(root, image=hotdog)
hotdog_label.grid(row=1, column=1)
pizza = PhotoImage(file='pizza.gif')
pizza.zoom(320) # still working on this part of the code.
#showin the hotdog
pizza_label = Label(root, image=pizza)
pizza_label.grid(row=1, column=4)
# displaying a menu for our pizzas.

l5 = tk.Label(root, text="Our Pizzas: Veggie Pizza, Sausage Pizza, Pepperoni pizza", font=("Arial", 15))

l5.place(x=50, y=200)

# displaying a menu for our hotdogs

l6 = tk.Label(root, text="Our Doggies: Reg Dog B or P, Turkey Dog, Chili - Cheese Dog", font=("Arial", 15))

l6.place(x=50, y=230)

l1 = tk.Label(root, text="Enter Pizza Order: (using comma)", font=("Arial", 15))

l1.place(x=50, y=280)

# entry box with font  and size

t1 = tk.Entry(root, font=("Arial", 15))

t1.place(x=380, y=280)  # position of entry box

l2 = tk.Label(root, text="Enter Doggie Order: (using comma)", font=("Arial", 15))

l2.place(x=50, y=310)

t2 = tk.Entry(root, font=("Arial", 15))

t2.place(x=380, y=310)

# function to calculate price of pizza and doggies

# doggies separately

def calc():
    s1 = t1.get()  # taking all the contents from 1st entry

    s2 = t2.get()  # taking all the contents from 2nd entry

    pizza = s1.split(sep=',')  # separating each item from s1

    hotdog = s2.split(sep=',')  # separating each item from s1

    len1 = len(pizza)  # finding the length(number of items or pizza)

    len2 = len(hotdog)  # finding the length(number of items or hot dogs)

    priceOfPizza = len1 * 9.99  # multiplying number of pizza with price of 1

    priceOfHotdog = len2 * 1.99  # multiplying number of hot dogs with price of 1

    # displaying in a message box

    s = 'price of pizza : {} price of hot dog : {}'.format(priceOfPizza, priceOfHotdog)

    messagebox.showinfo('price of pizza and hot dog', s)

    # returning price of pizza ,hot dog ,list of pizza names and hot dog names

    return priceOfPizza, priceOfHotdog, pizza, hotdog


def total():
    # collecting price of pizzas, hot dogs and names of pizza and hot dogs

    pr_pizza, pr_hotdog, pizza, hotdog = calc()

    total = pr_pizza + pr_hotdog  # finding total price

    s = 'Total price : {:5.2f}'.format(total)

    child_w = Toplevel(root)  # creating another window

    child_w.geometry("350x350")  # size of child window

    child_w.grid_location(x=300, y=300)  # location of child window

    child_w.title("total price")  # title of the window

    # creating label widgets

    label_child = Label(child_w, text=s, font=('Helvetica 15'))

    label_child.grid(row=1, column=1)  # positioning the label

    l2 = Label(child_w, text="Thank you! Your total is listed above.", font=('Helvetica 15'))

    l2.place(x=20, y=100)  # positioning the label

    s2 = "Pizza: " + ' '.join(pizza) + " " + "\n" + "Hotdog: " + ' '.join(hotdog)

    l3 = Label(child_w, text=s2, font=('Helvetica 15'))

    l3.place(x=20, y=150)  # positioning the label

# creating the buttons

# click this button to calculate price of pizza and

# hot dog separately

b1 = tk.Button(root, text="Calculate P + D.", command=calc, font=("Arial", 15))

b1.place(x=100, y=380)

# click this button to calculate total price of pizza and

# hot dog

b2 = tk.Button(root, text="Calculate Your Total Price.", command=total, font=("Arial", 15))

b2.place(x=100, y=420)

# click this button to exit from the program

b3 = tk.Button(root, text="Exit.", command=root.destroy, font=("Arial", 15))

b3.place(x=100, y=460)

# starting the main window

root.mainloop()
