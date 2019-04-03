from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("D-eye-abetes APP")

        self.label = Label(master, text="Home Page")
        # self.label.pack()

        self.aim_photo = Button(master, text="Aim/Photo Mode", command=self.greet)
        # self.aim_photo.pack(side = LEFT)

        self.view_images = Button(master, text="View Images", command=master.quit)
        # self.view_images.pack(side = BOTTOM)

        self.shut_down = Button(master, text="Shut Down", command = self.greet)
        # self.shut_down.pack(side = RIGHT)

        self.label.grid(columnspan=3, sticky=N)
        self.aim_photo.grid(row=1)
        self.view_images.grid(row=1, column=1)
        self.shut_down.grid(row=1, column=2)


    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
