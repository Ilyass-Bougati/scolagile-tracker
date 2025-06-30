import tkinter as tk
from tkinter import ttk, messagebox
from tracker import track
import threading


def on_track():
    username = username_entry.get()
    password = password_entry.get()
    # Add your tracking logic here
    args = (username, password)
    trackerThread = threading.Thread(target=track, args=args, daemon=True)
    trackerThread.start()
    messagebox.showinfo("Info", "The tracker is running in the background now!")
    track_button.destroy()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to close the application?"):
        print("Application closed by user")  # Add any cleanup code here
        root.destroy()

# Create main window
root = tk.Tk()
root.title("Scolagile Tracker")
root.geometry("200x200")
root.resizable(False, False)

# Set the close window listener
root.protocol("WM_DELETE_WINDOW", on_closing)
root.iconbitmap('icon/exe.ico')

# Style configuration for a clean look
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=('Helvetica', 10))
style.configure("TButton", font=('Helvetica', 10))

# Main frame
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Username field
username_label = ttk.Label(main_frame, text="Username:")
username_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

username_entry = ttk.Entry(main_frame, width=25)
username_entry.grid(row=1, column=0, pady=(0, 15))
username_entry.focus()

# Password field
password_label = ttk.Label(main_frame, text="Password:")
password_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))

password_entry = ttk.Entry(main_frame, width=25, show="•")
password_entry.grid(row=3, column=0, pady=(0, 20))

# Track button
track_button = ttk.Button(main_frame, text="Track", command=on_track)
track_button.grid(row=4, column=0)

# Bind Enter key to track button
root.bind('<Return>', lambda event: on_track())

root.mainloop()