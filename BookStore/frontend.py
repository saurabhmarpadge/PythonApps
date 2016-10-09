from Tkinter import *
import backend

def view_command():
    list1.delete(0,END)  # deletes everything from indices 0 to END in list1 so that everytime the view all button is pressed,the results are not appended
    for row in backend.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):  # get the string from the entry fields using get()
        list1.insert(END,row)
        

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())  # simply insert the strings from entry fields
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))  # display the added entry - give it in a list otherwise the display will be on many lines


def get_selected_row(event):
    global selected_tuple  # make it global so that it can be accessed by delete_command()
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    #print(index)  # interesting output in the terminal - just for learning purpose
    #print(selected_tuple)
    #return selected_tuple
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])



def delete_command():
    backend.delete(selected_tuple[0])  # the id will be passed to the backend's delete function


def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())  # the updated strings of the entry fields are passed

window = Tk()

window.wm_title("Book Store")

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)


title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)


list1 = Listbox(window,height=10,width=60)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


# bind function for the list1 to get the id of the selected item
list1.bind('<<ListboxSelect>>',get_selected_row)



b1 = Button(window,text="View all",width=18,command=view_command)  # the view_command function will get use backend.view's output to put it into the listbox
b1.grid(row=2,column=3)

b2 = Button(window,text="Search entry",width=18,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add entry",width=18,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update selected",width=18,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete selected",width=18,command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=18,command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()