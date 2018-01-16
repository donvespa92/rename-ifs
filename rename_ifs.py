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
        self.entry_tagsolid = tk.Entry(self.frame_tags,width=30)
        self.label_tagfluid = tk.Label(self.frame_tags,text='Fluid domain tag')
        self.entry_tagfluid = tk.Entry(self.frame_tags,width=30)
        
        self.label_tagssif = tk.Label(self.frame_tags,text='Solid Solid interface tag')
        self.entry_tagssif = tk.Entry(self.frame_tags,width=30)
        self.label_tagffif = tk.Label(self.frame_tags,text='Fluid Fluid interface tag')
        self.entry_tagffif = tk.Entry(self.frame_tags,width=30)
        self.label_tagfsif = tk.Label(self.frame_tags,text='Fluid Solid interface tag')
        self.entry_tagfsif = tk.Entry(self.frame_tags,width=30)
        
        self.button_write = tk.Button(
                self.frame_tags,
                text='Write',
                height=2)
        

class AppRenameIfs(tk.Frame):
    def __init__(self,master):       
        tk.Frame.__init__(self,master)
        self.master = master
        self.master.option_add("*Font", "Arial 12")
        self.mainframe = tk.Frame(self.master)
        self.mainframe.pack(fill='both',expand=1)
        
        
        self.fp = filepaths(self)
        self.fp.frame_filepaths.pack(fill='both',expand=1,padx=5,pady=5)
        self.fp.label_inputfile.grid(row=1,column=1,sticky='W')
        self.fp.entry_inputfile.grid(row=2,column=1,sticky='NSEW')
        self.fp.label_outputfile.grid(row=3,column=1,sticky='W')
        self.fp.entry_outputfile.grid(row=4,column=1,sticky='NSEW')
        self.fp.button_selectinput.grid(row=2,column=2,sticky='NSEW')
        self.fp.button_selectoutput.grid(row=4,column=2,sticky='NSEW')

        self.tags = define_tags(self)
        self.tags.frame_tags.pack(fill='both',expand=1,padx=5,pady=5)
        self.tags.label_tagsolid.grid(row=1,column=1,sticky='E')
        self.tags.entry_tagsolid.grid(row=1,column=2,sticky='NSEW',padx=5,pady=5)
        self.tags.label_tagfluid.grid(row=2,column=1,sticky='E')
        self.tags.entry_tagfluid.grid(row=2,column=2,sticky='NSEW',padx=5,pady=5)
        self.tags.label_tagssif.grid(row=3,column=1,sticky='E')
        self.tags.entry_tagssif.grid(row=3,column=2,sticky='NSEW',padx=5,pady=5)
        self.tags.label_tagffif.grid(row=4,column=1,sticky='E')
        self.tags.entry_tagffif.grid(row=4,column=2,sticky='NSEW',padx=5,pady=5)
        self.tags.label_tagfsif.grid(row=5,column=1,sticky='E')
        self.tags.entry_tagfsif.grid(row=5,column=2,sticky='NSEW',padx=5,pady=5)
        
        self.tags.button_write.grid(row=6,column=1,columnspan=2,sticky='NSEW')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Rename interfaces')
    AppRenameIfs(root).pack()
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()       

