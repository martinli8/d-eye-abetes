import Tkinter as tk
import tkMessageBox
from Tkinter import *
from simple_function import *
from PIL import ImageTk, Image
import numpy as np
import camAc as cAc
class Page(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
	def show(self):
		self.lift()


class Page1(Page):
   def __init__(self, *args, **kwargs):
	   global display
	   from simple_function import counter
	   Page.__init__(self, *args, **kwargs)

	   photoEnter = tk.Button(self,text = "Aim mode", command = self.enterAimMode)
	   photoEnter.grid(row=1, column=1)
	   photoExit = tk.Button(self,text = "Photo Mode/Exit Aim", command = self.exitPhotoMode)
	   photoExit.grid(row=1, column=2)


	   global even
	   even = True

	   global removeBoolean
	   removeBoolean = False

   def enterAimMode(self):
		global display
		display = True
		self.refresh()


		brightenButton.grid_remove()
		dimButton.grid_remove()
		saveButton.grid_remove()


   def exitPhotoMode(self):
		global display
		display = False

		self.displayCurrentImage()
		self.displayImageModButtons()


   def saveCurrentImage(self):
	   print("Saved Current Image")

   def displayCurrentImage(self):
	   print("displaying current/updated Image")

   def displayImageModButtons(self):
	   global brightenButton
	   global dimButton
	   global saveButton

	   brightenButton = tk.Button(self, text = "Brighten", command = self.brightnessIncrease)
	   dimButton = tk.Button(self, text = "Dim", command = self.brightnessDecrease)
	   saveButton = tk.Button(self, text = "Save", command = self.saveCurrentImage)

	   brightenButton.grid(row = 2, column = 1)
	   dimButton.grid(row=2,column=2)
	   saveButton.grid(row=2, column=3)


   def brightnessIncrease(self):
	   print("brightnessIncreased")
	   self.displayCurrentImage()

   def brightnessDecrease(self):
	   print("brightnessDecreased")
	   self.displayCurrentImage()

   def refresh(self):
	   global even
	   global removeBoolean
	   global picture
	   if removeBoolean is True:
		   picture.grid_remove()
	   if even == True:
			data = cAc.getmyImg()

			im = Image.fromarray(data)
			ph = ImageTk.PhotoImage(im)

			picture = Label(self, image=ph) #pic 1
			picture.image=ph
			picture.grid(row=3,column=2)
			even = True
			removeBoolean = True;
	   else:
		   im = Image.open("/Users/Shared/BME436/app1.jpg")
		   ph = ImageTk.PhotoImage(im)

		   picture = Label(self, image=ph) #pic 1
		   picture.image=ph
		   picture.grid(row=3,column=2)

		   even = True


	   global display

	   if display:
		   self.after(500, self.refresh)


class Page2(Page):
   def __init__(self, *args, **kwargs):
	   Page.__init__(self, *args, **kwargs)
	   #still need to finish logic for individual file names and saving to array

	   #im = Image.open("/Users/Shared/BME436/app.jpg")
	   #ph = ImageTk.PhotoImage(im)

	   #label = Label(self, image=ph) #pic 1
	   #label.image=ph
	   #label.grid(row=2)

	   #label1 = Label(self, image=ph) #pic2
	   #label1.image=ph
	   #label1.grid(row=2, column=1)

	   #label1 = Label(self, image=ph) #pic3
	   #label1.image=ph
	   #label1.grid(row=2, column=2)

	   #label2 = Label(self, text="Procured Images")
	   #label2.grid(row=1, column=1)


class Page3(Page):
   from simple_function import page3_functions
   def __init__(self, *args, **kwargs):
	   Page.__init__(self, *args, **kwargs)
	   turnOffLED = tk.Button(self, text = "turn OFF LED", command = self.page3_functions)
	   ExitProgram = tk.Button(self, text = "ExitProgram", command = self.quit)

	   turnOffLED.pack()
	   ExitProgram.pack()

class MainView(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		p1 = Page1(self)
		p2 = Page2(self)
		p3 = Page3(self)
		self.master = master
		self.label = Label(master, text="D-eye-abetes Home Page")


		buttonframe = tk.Frame(self)
		container = tk.Frame(self)
		buttonframe.pack(side="top", fill="x", expand=False)
		container.pack(side="top", fill="both", expand=True)

		p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

		b1 = tk.Button(buttonframe, text="Aim/Photo Mode", command=p1.lift)
		b2 = tk.Button(buttonframe, text="View Images", command=p2.lift)
		b3 = tk.Button(buttonframe, text="Shut down", command=p3.lift)

		self.label.pack()
		b1.pack(side="left")
		b2.pack(side="left")
		b3.pack(side="left")

		p1.show()

#if __name__ == "__main__":
def runUI():
	root = tk.Tk()
	main = MainView(root)
	main.pack(side="top", fill="both", expand=True)
	root.wm_geometry("400x400")
	root.mainloop()
