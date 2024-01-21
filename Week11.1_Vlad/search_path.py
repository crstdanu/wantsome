import tkinter as tk
from tkinter import filedialog


def open_file_dialog():
    # Open a file dialog for selecting a directory
    selected_directory = filedialog.askdirectory()

    # Do something with the selected directory (e.g., print it)
    print("Selected directory:", selected_directory)


# Create the main Tkinter window
root = tk.Tk()
root.title("Path Selection Example")

# Create a button to trigger the file dialog
button = tk.Button(root, text="Select Path", command=open_file_dialog)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
