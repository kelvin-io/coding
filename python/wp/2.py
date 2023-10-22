from PIL import Image

# Load the image
image = Image.open('.png').convert('RGBA')

# Create a color layer with the desired color and alpha value
color = (0, 0, 0, int(0.6 * 255))  # Green color with alpha value
color_layer = Image.new('RGBA', image.size, color)

# Blend the color layer with the image
output_image = Image.alpha_composite(image, color_layer)

# Save the output image
output_image.save('red_output_layer_added.png')