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
        global img
        self.panel = None
        #from simple_function import counter
        Page.__init__(self, *args, **kwargs)
        #self.pack()
        photoEnter = tk.Button(self,text = "Aim mode", command = self.enterAimMode, height = 2)
        photoEnter.grid(row=0, column=3)
        photoExit = tk.Button(self,text = "Photo Mode", command = self.exitPhotoMode, height = 2)
        photoExit.grid(row=0, column=4)

        #canvas = Canvas(self,width= 800, height =480)
        #canvas.pack()
        global im
        global data
        data = 0
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
        global im
        cAc.savImg(im)
        print("Saved Current Image")

   def displayCurrentImage(self):
	   print("displaying current/updated Image")

   def displayImageModButtons(self):
	   global brightenButton
	   global dimButton
	   global saveButton

	   brightenButton = tk.Button(self, text = "Brighten", command = self.brightnessIncrease, height = 10)
	   dimButton = tk.Button(self, text = "Dim", command = self.brightnessDecrease, height = 10, width = 10)
	   saveButton = tk.Button(self, text = "Save", command = self.saveCurrentImage, height = 2,width = 10)

	   brightenButton.grid(row = 3, column = 1)
	   dimButton.grid(row=3,column=3)
	   saveButton.grid(row=0, column=2)


   def brightnessIncrease(self):
	   print("brightnessIncreased")
	   global data
	   global img
	   global im
	   myhelp = 10*np.ones((1024,1280))
	   data = data + myhelp
	   im = Image.fromarray(data)
	   imDS = im.resize((800, 480))
	   img = ImageTk.PhotoImage(imDS)
	   self.panel.configure(image=img)
	   self.panel.image = img
	   

   def brightnessDecrease(self):
	   print("brightnessDecreased")
	   global data
	   global img
	   myhelp = -10*np.ones((1024,1280))
	   data = data + myhelp
	   im = Image.fromarray(data)
	   imDS = im.resize((800, 480))
	   img = ImageTk.PhotoImage(imDS)
	   self.panel.configure(image=img)
	   self.panel.image = img

   def refresh(self):
        global cam
        global removeBoolean
        global im
        global img
        global data
        
      #  if removeBoolean == True:
               # picture.grid_remove()
           
        data = cAc.getmyImg(cam)
        #print cam
        #print data
        im = Image.fromarray(data)
        imDS = im.resize((800, 480))
        img = ImageTk.PhotoImage(imDS)
        del imDS
        
        #self.canvas.create_image(20,20, anchor="nw", image=img)
        #self.canvas.image = self.img
        
##        picture = Label(self, image=img) #pic 1
####        picture.image=ph
##        picture.grid(row=3,column=3)
##        removeBoolean = True;

        if self.panel is None:
                self.panel = Label(self, image = img)
                self.panel.image = img
                self.panel.grid(row=3, column=2)

        else:
                self.panel.configure(image=img)
                self.panel.image = img
                        
        
        global display

        if display:
           self.after(40, self.refresh)


class Page2(Page):
        def __init__(self, *args, **kwargs):
                Page.__init__(self, *args, **kwargs)
                #still need to finish logic for individual file names and saving to array

                genIms = tk.Button(self,text = "Refresh", command = self.gIm)
                genIms.grid(row=0, column=0)

        def gIm(self):
                pics = cAc.getimgs()
                #im = Image.open("/Users/Shared/BME436/app.jpg")
                #ph = ImageTk.PhotoImage(im)
                i = 1
                j = 1
                print(pics)
                for paths in pics:
                        bim = Image.open('/home/pi/Desktop/436/d-eye-abetes/Photos/' +paths)
                        print(bim)
                        imDD = bim.resize((400, 240))
                        ph = ImageTk.PhotoImage(imDD)
                        
                        label = Label(self, image=ph)
                        label.image = ph
                        label.grid(row=i, column = j)
                        i = i+1
                        if i == 4:
                                i = 1
                                j = j + 1
                        
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
	   turnOffLED = tk.Button(self, text = "turn OFF LED", command = self.page3_functions, height = 10)
	   ExitProgram = tk.Button(self, text = "ExitProgram", command = self.quit, height = 10)

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
def runUI(mycam):
        global cam
        cam = mycam
        root = tk.Tk()
        #canvas = Canvas(root,width= 800, height =480)
        #canvas.pack()
        
        main = MainView(root)
        main.pack(side="top", fill="both", expand=True)
        root.wm_geometry("400x400")
        root.mainloop()
