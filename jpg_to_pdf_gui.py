import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk, Image
import os
from tkinter import filedialog

# Functions

def disable(btn):
    btn['state']='disabled'
    btn['bg']='Silver'

def enable(btn, clr):
    btn['state']='active'
    btn['bg']=clr

def hide(btn):
    btn.grid_forget()

def show(btn):
    btn.grid(row=4, pady=15)

def vers(text, n):

    lenf = len(files['filename'])

    if(n==0):
        text['text']='Ready to upload'
    if(n==1):
        text['text']= ('Selected ' +str(lenf)+ ' files - Convert it!')
    if(n==2):
        text['text']='Converted! You can Download PDF'

files = {}

# UPLOAD IMAGES
def upload_imgs():
    global files
    files['filename']=filedialog.askopenfilenames(filetypes=[('JPG','*.jpg'), ('PNG','*.png'), ('JPEG','*.jpeg')],
    initialdir=os.getcwd(), title='Select File/Files')

    if len(files['filename'])!=0:
        enable(convert_button, downbg)
        vers(dtext, 1)

img_list = []

# CONVERT IMAGES
def convert():
    global img_list
    for file in files['filename']:
        img_list.append(Image.open(file).convert('RGB'))

    hide(convert_button)
    show(download_button)
    enable(download_button, downbg)
    disable(upload_button)
    vers(dtext, 2)

# DOWNLOAD PDF
def saveas():
    try:
        global files
        global img_list
        save_file_name = filedialog.asksaveasfilename(filetypes = [('PDF', '*.pdf')], initialdir = os.getcwd(), title='Save File')
        img_list[0].save(f'{save_file_name}.pdf', save_all=True, append_images = img_list[1:])
        
        hide(download_button)
        show(convert_button)
        disable(convert_button)
        enable(upload_button, upbg)
        vers(dtext, 0)
        files = {}
        img_list = []

    except Exception:

        hide(download_button)
        show(convert_button)
        disable(convert_button)
        enable(upload_button, upbg)
        vers(dtext, 0)
        files = {}
        img_list = []

# Design GUI
win = tk.Tk()
win.title('IMG to PDF Converter')
win.geometry('400x600')
win.iconbitmap('conv.ico')
win.resizable(0,0)

mybg = "DarkSlateBlue"

win["bg"] = mybg

# Image
canvas = Canvas(win, width=256, height=256, bg=mybg)
canvas.grid(row=0, column=0, sticky=tk.N, padx=0, pady=10)

main_img = ImageTk.PhotoImage(Image.open('converter.png'))
canvas.create_image(128, 128, image = main_img)
canvas.config(highlightthickness=0)

# Description
text = tk.Label(win, text='IMG to PDF Converter', width=20, height=1, font=('Calibri', 25, 'bold'), bg=mybg, fg='DarkOrange')
text.grid(row=1, column=0, padx=0, pady=10)

# Dinamic text
dtext = tk.Label(win, text='Ready to upload', width=30, height=1, font=('Calibri', 14, 'bold'), bg=mybg, fg='white')
dtext.grid(row=2, column=0, padx=0, pady=15)

# Upload botton
upbg = 'DarkTurquoise'
upload_button = tk.Button(win, text='UPLOAD IMAGES', width=25, height=2, font=('Calibri', 17, 'bold'), bg=upbg, fg='Black', command=upload_imgs)
upload_button.grid(row=3, column=0, padx=43, pady=0)

# Convert button
downbg = 'DarkOrange'
convert_button = tk.Button(win, text='CONVERT', width=25, height=2, font=('Calibri', 17, 'bold'), bg=downbg, fg='Black', command=convert)
convert_button.grid(row=4, column=0, pady=15)
disable(convert_button)

# Download button
download_button = tk.Button(win, text='DOWNLOAD PDF', width=25, height=2, font=('Calibri', 17, 'bold'), bg=downbg, fg='Black', command=saveas)
disable(download_button)
hide(download_button)

win.mainloop()