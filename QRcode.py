import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

# මේvariable එකට generate කරපු QR එක store වෙනව
generated_qr = None


# this function for generate the QR code
def generate_qr():
    global generated_qr

    text = entry.get()   #get the link

    if text == "":
        messagebox.showerror("Error", "Please enter some text")
        return

    # Create QR image
    generated_qr = qrcode.make(text)

    # Resize image for display
    resized_image = generated_qr.resize((200, 200))

    # Convert image to Tkinter format
    tk_image = ImageTk.PhotoImage(resized_image)

    # Show image in label
    qr_label.config(image=tk_image)
    qr_label.image = tk_image


# Function to download QR image we have generated
def download_qr():
    if generated_qr is None:
        messagebox.showerror("Error", "Please generate QR first")
        return

    # Open save dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png"
    )

    if file_path:
        generated_qr.save(file_path)
        messagebox.showinfo("Success", "QR Code saved successfully")


# --------This is the Main Window --------
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")

# Title
title_label = tk.Label(root, text="QR Code Generator", font=("Arial", 18))
title_label.pack(pady=20)

# Input box
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate QR", command=generate_qr)
generate_button.pack(pady=10)

# Download button
download_button = tk.Button(root, text="Download QR", command=download_qr)
download_button.pack(pady=10)

# Label to display QR image
qr_label = tk.Label(root)
qr_label.pack(pady=20)

root.mainloop()
