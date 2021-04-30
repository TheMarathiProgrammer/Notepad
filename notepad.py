import tkinter as tk 
from tkinter import *
from tkinter import filedialog
root = tk.Tk()
root.title('Notepad')
root.geometry('700x380')

text_scroll = tk.Scrollbar(root)
text_scroll.pack(side=RIGHT,fill=Y)

text_area = tk.Text(root,width=100,height=25,yscrollcommand = text_scroll.set)
text_area.pack()
text_scroll.config(command=text_area.yview)
global name 
name=False
def new_file():
	text_area.delete(1.0,END)
	root.title('Untitled - Notepad')

def open_file():
	text_area.delete(1.0,END)
	text_file = filedialog.askopenfilename(initialdir='C:/Users/hp/Desktop/work/Mini Projects/Youtube',title='Open',filetypes=(('Text Files','*.txt'),('HTML Files','*.html'),('Python Files','*.py'),('All Files','*.*')))
	if text_file:
		global name
		name = text_file
		name = name.replace('C:/Users/hp/Desktop/work/Mini Projects/Youtube/','')
	root.title(f'{name} -Notepad')
	text_file = open(name,'r')
	stuff = text_file.read()
	text_area.insert(END,stuff)
	text_file.close()

def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension='.*',initialdir='C:/Users/hp/Desktop/work/Mini Projects/Youtube',title='Save As',filetypes=(('Text Files','*.txt'),('HTML Files','*.html'),('Python Files','*.py'),('All Files','*.*')))
	if text_file:
		global name
		name = text_file
		name = name.replace('C:/Users/hp/Desktop/work/Mini Projects/Youtube/','')
	root.title(f'{name} -Notepad')
	text_file = open(text_file,'w')
	text_file.write(text_area.get(1.0,END))	
	text_file.close()

def save_file():
	global name
	if name:
		text_file = open(name,'w')
		text_file.write(text_area.get(1.0,END))
		text_file.close
		root.title(f'Saved: {name} -Notepad')

	else:
		save_as_file()

def cut_text():
	global select
	select = text_area.selection_get()
	text_area.delete('sel.first','sel.last')

def copy_text():
	global select
	select = text_area.selection_get()

def paste_text():
	cursur = text_area.index(INSERT)
	print(cursur)
	text_area.insert(cursur,select)


my_menu = tk.Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_file)
file_menu.add_command(label='Save As',command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.quit)

edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Cut',command=cut_text)
edit_menu.add_command(label='Copy',command=copy_text)
edit_menu.add_command(label='Paste',command=paste_text)
root.mainloop()