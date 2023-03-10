import tkinter
from tkinter.filedialog import asksaveasfilename
import customtkinter
from PIL import Image, ImageTk
import qrcode
import os

# function to create qr code from text
def createQR(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

# root
root = customtkinter.CTk()
root.geometry('600x497')
root.title('QR Mate')
root.resizable(False, False)
root.iconphoto(False, ImageTk.PhotoImage(Image.open('favicon.png')))

# title label
labelTitle = customtkinter.CTkLabel(master=root, text='QR Mate', font=('arial', 34))
labelTitle.pack(pady=8)

# frame for generating QR code
frameGenerateQR = customtkinter.CTkFrame(master=root, width=580, height=100)
frameGenerateQR.pack()

# label for generating QR code
labelGenerateQR = customtkinter.CTkLabel(master=frameGenerateQR, text='Generate QR code', font=('arial', 14))
labelGenerateQR.pack(padx=230, pady=5)

# nested frame for input buttons
nestedFrame = customtkinter.CTkFrame(master=frameGenerateQR, bg_color='#2b2b2b', fg_color='#2b2b2b')
nestedFrame.pack()

# entry for text for QR
entryTextQR = customtkinter.CTkEntry(master=nestedFrame, placeholder_text="Enter your website URL or any text", width=463)
entryTextQR.pack(pady=5, side=tkinter.LEFT)

imageQR = None
def generateQRCode():
    global imageQR, buttonClearQR, buttonSaveQR
    buttonSaveQR.configure(state=tkinter.NORMAL)
    buttonClearQR.configure(state=tkinter.NORMAL)
    imageQR = createQR(entryTextQR.get())
    imageQR.save('temp_img.png')
    labelImageQR.configure(image=ImageTk.PhotoImage(Image.open('temp_img.png')))
    os.remove('temp_img.png')

# generate buttom for QR
buttonGenerateQR = customtkinter.CTkButton(master=nestedFrame, text='Generate', width=1, command=generateQRCode)
buttonGenerateQR.pack(side=tkinter.LEFT, pady=5)

#labelImg = ImageTk.PhotoImage(image=imageQR)
labelImageQR = customtkinter.CTkLabel(master=frameGenerateQR, image=ImageTk.PhotoImage(Image.open('blank.png')), text="")
labelImageQR.pack(pady=10)

# another nested frame for input buttons
nestedFrame2 = customtkinter.CTkFrame(master=frameGenerateQR, bg_color='#2b2b2b', fg_color='#2b2b2b')
nestedFrame2.pack(pady=5)

def clearQR():
    global labelImageQR, buttonSaveQR, buttonClearQR
    buttonSaveQR.configure(state=tkinter.DISABLED)
    buttonClearQR.configure(state=tkinter.DISABLED)
    labelImageQR.configure(image=ImageTk.PhotoImage(Image.open('blank.png')))

# clear button for setting QR to blank again
buttonClearQR = customtkinter.CTkButton(master=nestedFrame2, text='Reset', width=1, command=clearQR, state=tkinter.DISABLED)
buttonClearQR.pack(side=tkinter.LEFT, pady=5)

def saveQR():
    global imageQR
    imageQR.save(asksaveasfilename(initialfile = 'QR.png', defaultextension=".png", filetypes=[("All Files","*.*"),("Image Files","*.png")])
)

# save button for saving image to PC
buttonSaveQR = customtkinter.CTkButton(master=nestedFrame2, text='Save', width=1, command=saveQR, state=tkinter.DISABLED)
buttonSaveQR.pack(side=tkinter.LEFT, pady=5, padx=10)

root.mainloop()