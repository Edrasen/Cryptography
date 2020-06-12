import cryptoutil
import tkinter 
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

input_file = ""
valdation_file = ""
key_file = ""

top = tkinter.Tk()
content = Text(top, width = 100)
Label1 = Label(top)
Label1.config(text="SELECTED KEY FILE: ")
ruta = Label(top)


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
	cryptoutil.cryptoutil(input_file)
	messagebox.showinfo("DONE!", "Procedure finished succesfully!")

def callbackVER():
	ver = (cryptoutil.validate_hash(input_file))
	print(ver)
	if ver == True:
		messagebox.showinfo("DONE!", "Files do match!")
	else:
		messagebox.showwarning("ERROR", "Files don't match")

def select_KeyFile():
	global key_file
	key_file = filedialog.askopenfilename()
	print(key_file)
	ruta.config(text=key_file)
	ruta.pack()

def callbackSign():
	global key_file
	cryptoutil.firmar(input_file,key_file)
	messagebox.showinfo("DONE!", "Signed file succesfully created!")

def callbackSign_Verif():
	flag = True
	flag = cryptoutil.validar_firma(input_file,key_file)
	if flag == True:
		messagebox.showinfo("Sign validated", "Message hash and decryption do match!")
	else:
		messagebox.showwarning("ERROR", "Info doesn't match")
	

m1 = PanedWindow(top, orient=VERTICAL)
m1.pack(fill = NONE, expand = 0)
m1.add(content)
m2 = PanedWindow(m1, orient = HORIZONTAL)
m2.pack()
m1.add(m2)

select_F = Button(top, text="Select a File", command=select_file)
select_F.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

Hash_B = Button(top, text="Hash File", command=callbackHASH)
Hash_B.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

Verify_B = Button(top, text="Verify Hash", command=callbackVER)
Verify_B.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

Sign_B = Button(top, text="Sign", command=callbackSign)
Sign_B.pack(side="bottom", fill="both",expand="no",padx="10",pady="10")

VerifySign_B =  Button(top, text="Verify Sign", command=callbackSign_Verif)
VerifySign_B.pack(side="bottom", fill="both",expand="no",padx="10",pady="10")

SelKey_B = Button(top, text="Select Key File", command=select_KeyFile)
SelKey_B.pack(side="bottom", fill="none",expand="no",padx="10",pady="10")

Label1.pack()
m2.add(select_F)
m2.add(Hash_B)
m2.add(Verify_B)
m2.add(Sign_B)
m2.add(SelKey_B)
m1.add(ruta)

top.mainloop()
