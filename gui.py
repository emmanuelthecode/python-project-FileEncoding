import tkinter as tk
from compressmodule import compress, decompress #Import both functions from that module
#In this, we create a Graphical User interface that would be used as a way to compress files in Python


def compression(i,o):#This was created to be used in the command for tkinter in the encoding and decoding for the GUI
    compress(i,o)

window = tk.Tk()#Creates a window
window.title("Compression engine")#Name of the window
window.geometry("600x400")#Size of the window

input_entry = tk.Entry(window)#This would be the input entry that takes in an input file.
output_entry = tk.Entry(window)#This is an entry that in an output entry or the file that it is going to be written to after compression.
button_compress = tk.Button(window, text="Compress")
label1 = tk.Label(window, text="File to be compressed:")#Label for where the text is going to be inputted.
label2 = tk.Label(window, text="Name of the compressed file:") #Final file name that would be written to.



button_compress.grid(row =2, column=1)
label1.grid(row=0, column=0)
input_entry.grid(row = 0, column=1)#Grid showing where the input_entry is.
label2.grid(row=1, column=0)
output_entry.grid(row=1, column=1)




window.mainloop()