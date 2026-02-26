import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("500x600")
app.title("QR Code Generator")
app.configure(fg_color="#EDEDED")

qr_image = None

def generate_qr():
    global qr_image
    data = entry.get()
    if data:
        qr = qrcode.make(data)
        qr = qr.resize((250, 250))
        qr_image = ImageTk.PhotoImage(qr)
        qr_label.configure(image=qr_image)

def download_qr():
    data = entry.get()

    if not data:
        messagebox.showerror("Error", "Please enter text or URL first.")
        return

    # Open save dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Save QR Code"
    )

    if file_path:
        qr = qrcode.make(data)
        qr.save(file_path)
        messagebox.showinfo("Success", "QR Code downloaded successfully!")


# ===== Card Frame =====
card = ctk.CTkFrame(app,
                    width=400,
                    height=550,
                    corner_radius=25,
                    fg_color="#F4F4F4")

card.pack(pady=40)
card.pack_propagate(False)

# ===== Title =====
title = ctk.CTkLabel(card,
                     text="QR Code Generator",
                     font=("Segoe UI", 24, "bold"),
                     text_color="#111111")
title.pack(pady=25)

# ===== Entry =====
entry = ctk.CTkEntry(card,
                     width=320,
                     height=40,
                     corner_radius=15,
                     placeholder_text="Enter URL here...")
entry.pack(pady=15)

# ===== Generate Button =====
generate_btn = ctk.CTkButton(card,
                             text="Generate QR",
                             width=220,
                             height=40,
                             corner_radius=20,
                             fg_color="#6FCF97",
                             hover_color="#57B884",
                             text_color="black",
                             command=generate_qr)
generate_btn.pack(pady=10)

# ===== Download Button =====
download_btn = ctk.CTkButton(card,
                             text="Download QR",
                             width=220,
                             height=40,
                             corner_radius=20,
                             fg_color="#6FCF97",
                             hover_color="#57B884",
                             text_color="black",
                             command=download_qr)
download_btn.pack(pady=5)

# ===== QR Image Display =====
qr_label = ctk.CTkLabel(card, text="")
qr_label.pack(pady=25)

app.mainloop()
