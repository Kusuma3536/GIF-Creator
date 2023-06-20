from PIL import Image

# List of image filenames in the order you want them to appear in the GIF
image_filenames = ["1.png", "2.png", "3.png"]

# Duration (in milliseconds) to display each image in the GIF
image_duration = 500

# Output GIF filename
output_filename = "animation.gif"

# Open the first image
first_image = Image.open(image_filenames[0])

# Create a GIF file using the first image as the base
first_image.save(
    output_filename,
    format="GIF",
    append_images=[],
    save_all=True,
    duration=image_duration,
    loop=0
)

# Open and append the remaining images to the GIF
for filename in image_filenames[1:]:
    image = Image.open(filename)
    image.save(
        output_filename,
        append_images=[image],
        save_all=True,
        duration=image_duration,
        loop=0
    )
