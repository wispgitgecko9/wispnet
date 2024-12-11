# Recreate the image from the text file with added debugging

# Create a new image to hold the pixel data
image = Image.new("RGB", image_size)
pixels = image.load()

# Read the text file and set pixel colors
with open(text_file_path, "r") as file:
    for y in range(image_size[1]):
        line = file.readline().strip().split()
        for x in range(image_size[0]):
            # Ensure hex_color is correctly formatted (strip any unwanted whitespace)
            hex_color = line[x].strip()
            if hex_color.startswith('#'):
                hex_color = hex_color[1:]  # Remove the '#' character

            # Check if hex_color is valid
            if len(hex_color) == 6:  # Valid hex color should have 6 characters
                try:
                    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))  # Convert #RRGGBB to RGB
                    pixels[x, y] = rgb_color
                except ValueError as e:
                    print(f"Error converting {hex_color} to RGB at ({x}, {y}): {e}")
            else:
                print(f"Invalid hex color at ({x}, {y}): {hex_color}")

# Save the rendered image
output_image_path = "rendered_image.png"
image.save(output_image_path)

output_image_path
