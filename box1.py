from Tkinter import * # python 2x
#import Tkinter
#from tkinter import * # python 3x
#from tkFileDialog import *
#import tkMessageBox, tkSimpleDialog
from tkFileDialog import *
import Tkinter, Tkconstants, tkFileDialog

def setup_inputs():
    initial_path = "D:\\LowerWabash\\Indna_wtlnd\\"
    name_box = "Database Setup"
    
    file_name = setup_window_box(initial_path, name_box)    #  <------------------  function
    print "file name: ",file_name

def setup_window_box(initial_path, name_box):
    class Demo:
        def __init__(self, top):
            self.name=""
            #####window1.geometry=("800x400+200+200")
            frame_e = Frame(height=200,width=900) #     MAIN BOX DIMENSION
            #frame_e.geometry=("650x600+200+200")
            frame_e.pack(padx=20,pady=20) #packing allows to get widgets

            txt1 = StringVar()
            txt1.set("Address:")  # FIRST LABEL
            label_1 = Label(window1, textvariable=txt1, fg="blue" ,height=2).place(x=0,y=10)#Tag position
                
            pre_address = "E:\\Lowerwabash" # NAME BY DEFAULT INSIDE THE BOX
            #self.t_name = StringVar(None)
            #self.t_name.set = pre_address
            self.t_name = StringVar(None)
            self.t_name.set(pre_address)

            text = Entry(window1, textvariable=self.t_name, width=120, bg="white") #BOX
            #text = Entry(window1, textvariable=self.t_name, width=60, bg="white")
            text.place(x=120,y=20)
            #text.pack()
            text.focus_force()

            nameButton = Button(window1, text="Open", command=self.Naming) # SECOND LABEL
            nameButton.place(x=850, y=15)#(side="bottom", padx=15, pady=15)
            #nameButton.pack(side=BOTTOM, anchor=S)
        
            nameButton = Button(window1, text="Accept", command=self.Closing) #THIRD LABEL
            nameButton.place(x=600, y=60)#(side="bottom", padx=15, pady=15)
            #nameButton.pack(side=BOTTOM, anchor=S)
        
        def Naming(self):   # THIS FUNCTION 
            #input_name = askdirectory()  # ASK FOLDER NAME (DIRECTORY)
            #input_name = askopenfilename() # ASK FILE NAME
            #input_name = askopenfilename(initialdir = "D:\\LowerWabash\\Indna_wtlnd\\",title = "Select file",filetypes = (("shape files","*.shp"),("all files","*.*"))) #ASK FILE WITH INITIALDIR
            input_name = askopenfilename(initialdir = initial_path,title = "Select file",filetypes = (("shape files","*.shp"),("all files","*.*"))) #ASK FILE WITH INITIALDIR
            # # SAVE FILE
            #input_name = tkFileDialog.asksaveasfilename(initialdir = "D:\\LowerWabash\\Indna_wtlnd\\",title = "Select file",filetypes = (("shapefiles","*.shp"),("jpeg files","*.jpg"),("all files","*.*")))

            #print (input_name)
            
            self.t_name.set(input_name)
            #text.delete(0,END)
            #text.insert(0,input_name)
        
            #self.name = self.t_name.get()
            self.name = input_name
            print self.name

        def Closing(self):
            if D.name =="":
                lbl_message = Label(window1, text="Select a directory", fg="red").place(x=300,y=100) # Condition of Closing
            else:
                window1.destroy()

            #print "input name: ",D.name
            #self.name = self.t_name.get()

#def setup_window_box():
    window1 = Tk()

    #window1.title("Database Setup") # Window tittle ########
    window1.title(name_box) # Window tittle ########
    window1.geometry=("800x400+200+200")
    D = Demo(window1)
    window1.mainloop()

    value_returned = D.name
    print "Name retrieved was:  ", value_returned
    return value_returned

if __name__ == "__main__":
    setup_inputs()

    #setup_window_box()

#### Help
# ARcMap Python add-in
# http://desktop.arcgis.com/es/arcmap/latest/analyze/python-addins/essential-python-add-in-concepts.htm
# Tkinter
# https://pythonspot.com/en/tk-file-dialogs/
