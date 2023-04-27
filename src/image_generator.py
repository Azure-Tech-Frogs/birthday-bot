import os
from PIL import Image, ImageOps, ImageDraw

# Open the generic birthday image using os module to find img folder path relative to this file
current_dir = os.path.dirname(__file__)
img_dir = os.path.join(current_dir, "../img")
birthday_image = Image.open(os.path.join(img_dir, "input", "birthday_image.jpg"))

# Open the profile picture
profile_picture = Image.open(os.path.join(img_dir, "input", "profile_picture.jpg"))

# Resize the profile picture to fit in the center of the birthday image
profile_picture = profile_picture.resize((500, 500))

# Create a mask to make the profile picture rounded
mask = Image.new(
    "L", profile_picture.size, 0
)  # mode 'L' (grayscale) with all pixels black
# mask.show()
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse(
    (0, 0) + profile_picture.size, fill=255
)  # draw a white ellipse on the mask
# mask.show()

# Apply the mask to the profile picture
rounded_profile_picture = ImageOps.fit(profile_picture, mask.size, centering=(0.5, 0.5))
rounded_profile_picture.putalpha(mask)
# rounded_profile_picture.show()

# Calculate the coordinates to paste the rounded profile picture at the center of the birthday image
x = (birthday_image.width - rounded_profile_picture.width) // 2
y = (birthday_image.height - rounded_profile_picture.height) // 2

# Paste the rounded profile picture onto the center of the birthday image
birthday_image.paste(rounded_profile_picture, (x, y), rounded_profile_picture)

# Save the new birthday image with the profile picture
birthday_image.save(os.path.join(img_dir, "output", "new_birthday_image.jpg"))
