from PIL import Image, ImageDraw, ImageFont
import datetime
import os

def generate_image(width, height, text):
    # Create a blank image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Choose the Arial font
    font_size = 1
    font = ImageFont.truetype("calibrib.ttf", font_size)

    # Increase the font size until the text fits the width of the image
    while font.getsize(text)[0] < width - 40:
        font_size += 1
        font = ImageFont.truetype("calibrib.ttf", font_size)

    # Calculate the position to center the text
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw the text with a black border
    outline_color = "black"
    border_size = 2
    for i in range(-border_size, border_size + 1):
        for j in range(-border_size, border_size + 1):
            draw.text((x + i, y + j), text, font=font, fill=outline_color)

    # Draw the text in white
    text_color = "black"
    draw.text((x, y), text, font=font, fill=text_color)

    return image

def save_image(image, filename):
    image.save(filename, "JPEG")

def generate_images(debug_mode=False, create_every_minute=False):
    # Get the current time
    now = datetime.datetime.now()

    if debug_mode:
        # Generate a single image for testing
        image = generate_image(600, 800, now.strftime("%H:%M"))
        save_image(image, "debug.jpg")
    else:
        # Create a directory to store the images
        os.makedirs("images", exist_ok=True)

        # Generate an image for each minute of the day
        for minute in range(1440):
            current_time = now + datetime.timedelta(minutes=minute)
            image = generate_image(600, 800, current_time.strftime("%H:%M"))
            filename = current_time.strftime("images/%H%M.jpg")
            save_image(image, filename)

# Example usage
generate_images(debug_mode=False, create_every_minute=True)
