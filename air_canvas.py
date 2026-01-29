import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

def open_next_file():
    # This function will be called when the START button is clicked
    # You can replace this with code to open another Python file or script
    try:
        subprocess.Popen(["python", "logic.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open the next file: {e}")

# Initialize the main window
root = tk.Tk()
root.title("Air Canvas")

# Create and configure the canvas
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Add background color to the main sections
canvas.create_rectangle(0, 0, 400, 600, fill="#FFFFFF")  # Left side background
canvas.create_rectangle(400, 0, 800, 600, fill="#4A6FA5")  # Right side background

# Add the Air Canvas text
canvas.create_text(200, 150, text="Air", font=("Helvetica", 32), fill="#0000FF")
canvas.create_text(200, 450, text="Canvas", font=("Helvetica", 32), fill="#FF0000")

# Add the image (logo)
# Here you need to provide the path to your image file
try:
    image = Image.open("image/prajwal.jpg")  # Load JPEG
    logo_image = ImageTk.PhotoImage(image)   # Convert for Tkinter
    #logo_image = tk.PhotoImage(file="image/prajwal.jpeg")
    canvas.create_image(200, 300, image=logo_image)  # Center image horizontally on the left side
except tk.TclError:
    messagebox.showerror("Error", "Image file not found. Please check the file path.")

# Add the START button
start_button = tk.Button(root, text="Save the Ink", font=("Helvetica", 32, "bold"), bg="#8A2BE2", fg="#FFFFFF",
                         padx=20, pady=10, relief="raised", bd=5, command=open_next_file)
canvas.create_window(600, 300, window=start_button)  # Center button in the right side rectangle

# Run the Tkinter event loop
root.mainloop()