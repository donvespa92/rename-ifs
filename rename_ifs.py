import tkinter as tk
import re
import ccl_templates as template
from tkinter import filedialog
import os

class filepaths(tk.Frame):
    def __init__(self,master):       
        tk.Frame.__init__(self,master)
        self.master = master
        self.frame_filepaths = tk.Frame(self.master)
        
        self.label_inputfile = tk.Label(self.frame_filepaths,text='Inputfile')
        self.entry_inputfile = tk.Entry(self.frame_filepaths,width=50)
        self.label_outputfile = tk.Label(self.frame_filepaths,text='Outputfile')
        self.entry_outputfile = tk.Entry(self.frame_filepaths,width=50)
        self.button_selectinput = tk.Button(self.frame_filepaths,text='Select')
        self.button_selectoutput = tk.Button(self.frame_filepaths,text='Select')

class define_tags(tk.Frame):
    def __init__(self,master):       
        tk.Frame.__init__(self,master)
        self.master = master 
        self.frame_tags = tk.Frame(self.master)
        
        self.label_tagsolid = tk.Label(self.frame_tags,text='Solid domain tag')
        self.entry_tagsolid = tk.Entry(self.frame_tags,width=50)
        self.label_tagfluid = tk.Label(self.frame_tags,text='Fluid domain tag')
        self.entry_tagfluid = tk.Entry(self.frame_tags,width=50)
        
        

class AppRenameIfs(tk.Frame):
    def __init__(self,master):       
        tk.Frame.__init__(self,master)
        self.master = master
        self.master.option_add("*Font", "Arial 12")
        


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Rename interfaces')
    AppRenameIfs(root).pack()
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()       

