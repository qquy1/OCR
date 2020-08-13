import pytesseract
# from PIL import Image
import tkinter as tk
from tkinter import filedialog

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

# ocr function
def convert():
    box_select.delete('1.0', tk.END) # to clear content box
    result_text.delete('1.0', tk.END)
    img = filedialog.askopenfilename()
    box_select.insert(tk.INSERT, img) # insert into the text box
    text = pytesseract.image_to_string(img)
    result_text.insert(tk.INSERT, text)

root = tk.Tk()

root.title("OCR App")

frame = tk.Frame(root, width=150)
frame.grid(row=0)

instruction = tk.Label(root, text="Please select the image you would like to perform OCR on:")
instruction.grid(row=1)

# output box to show which image is selected
box_select = tk.Text(root, height=1)
box_select.grid(row=2)

# select img button
button_select = tk.Button(root,
                          text="Select",
                          command=convert)
button_select.grid(row=3)

# result text box
result_text = tk.Text(root)
result_text.grid(row=4)

root.mainloop()