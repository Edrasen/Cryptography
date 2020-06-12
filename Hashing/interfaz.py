import program2_1
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

input_file = ""
valdation_file = ""

top = tkinter.Tk()
content = Text(top)
content2 = Text(top)


def select_file():
	global input_file
	# open a file chooser dialog and allow the user to select an input
	path = filedialog.askopenfilename()
	print(path)
	file = open(str(path), "r")
	for line in file:
		content.insert(INSERT, line)
	
	input_file = str(path)
	content.pack()	
	return path

def callbackHASH():
	program2_1.hashing(input_file)
	messagebox.showinfo("EXITO", "Procedure finished succesfully!")

def callbackVER():
	ver = (program2_1.validate_hash(input_file))
	print(ver)
	if ver == True:
		messagebox.showinfo("EXITO", "Files do match!")
	else:
		messagebox.showwarning("ERROR", "Files don't match")
	

m1 = PanedWindow(top, orient=VERTICAL)
m1.pack(fill = BOTH, expand = 0)
m1.add(content)
m2 = PanedWindow(m1, orient = HORIZONTAL)
#m3 = PanedWindow(m1, orient= VERTICAL)
m1.add(m2)
#m1.add(m3)

#content.insert(INSERT, )

select_F = Button(top, text="Select a File", command=select_file)
select_F.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")
Hash_B = Button(top, text="Hash File", command=callbackHASH)
Hash_B.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

Verify_B = Button(top, text="Verify File", command=callbackVER)
Verify_B.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

m2.add(select_F)
m2.add(Hash_B)
m2.add(Verify_B)
#m3.add(content2)
# Code to add widgets will go here...
top.mainloop()
