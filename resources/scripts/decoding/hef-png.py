import tkinter as tk
from tkinter import filedialog
from PIL import Image
import datetime

# WISPNET Theme Colors
BACKGROUND_COLOR = "#f4f4f4"  # light gray background
TEXT_COLOR = "#333333"  # dark gray text
FONT = ("Helvetica", 14)

def open_hex_file():
    # Function to open and process the hex file
    file_path = filedialog.askopenfilename(filetypes=[
        ("HEI Files", "*.hei"),   # Allow only .hei files
        ("Any File", "*.*"),   # Allow any file
        ("Text Files", "*.txt")  # Allow only .txt files
    ])
    if file_path:
        # Open the hex file and process it
        with open(file_path, "r") as file:
            hex_data = file.read()
        # Generate and show the image from the hex data (using previous code)
        generate_image(hex_data)

def generate_image(hex_data):
    # Set image size (assuming 300x300 for now)
    image_size = (300, 300)

    # Create a new image to hold the pixel data
    image = Image.new("RGB", image_size)
    pixels = image.load()

    # Read the hex values and assign them to the image pixels
    for y in range(image_size[1]):
        line = hex_data[y].strip().split()  # Get the hex values for the row
        for x in range(image_size[0]):
            hex_color = line[x].strip()
            if hex_color.startswith('#'):
                hex_color = hex_color[1:]  # Remove the '#' character if it exists

            if len(hex_color) == 6:  # Ensure it's a valid hex color
                # Convert hex to RGB
                rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                pixels[x, y] = rgb_color  # Set the pixel color

    # Get the current date and format it as YYMMDD
    current_date = datetime.datetime.now().strftime("%y%m%d")

    # Save the generated image with the current date as part of the filename
    image.save(f"{current_date}_output_image.png")

    # Show the generated image
    image.show()

# Create the root window
root = tk.Tk()
root.title("WISPNET Hex Color Image Renderer")  # Set window title
root.geometry("400x400")  # Set window size
root.configure(bg=BACKGROUND_COLOR)  # Set background color of the window

# Add a label
label = tk.Label(root, text="Select a Hex File to Render", font=("Helvetica", 12), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
label.pack(padx=20, pady=20)

# Add a normal, unstyled button
button = tk.Button(root, text="Open Hex File", command=open_hex_file, font=FONT)
button.pack(padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()
