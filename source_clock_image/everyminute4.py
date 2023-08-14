from PIL import Image, ImageDraw, ImageFont
import datetime
import os

def generate_image(width, height, text):
    # Create a blank image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Choose the Arial font
    font_size = 400  # Adjust the font size as desired
    font = ImageFont.truetype("calibrib.ttf", font_size)

    # Calculate the position to center the text
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Split the text into hour and minute parts
    hour_text, minute_text = text.split(":")
    hour_width, hour_height = draw.textsize(hour_text, font=font)
    minute_width, minute_height = draw.textsize(minute_text, font=font)

    # Calculate the positions for hour and minute texts
    hour_x = (width - hour_width) // 2
    hour_y = (height - hour_height - minute_height) // 2 - 10  # Adjust the vertical spacing between hour and minute
    minute_x = (width - minute_width) // 2
    minute_y = hour_y + hour_height + 10  # Adjust the vertical spacing between hour and minute

    # Draw the hour text with a black border
    hour_outline_color = "black"
    hour_border_size = 2
    for i in range(-hour_border_size, hour_border_size + 1):
        for j in range(-hour_border_size, hour_border_size + 1):
            draw.text((hour_x + i, hour_y + j), hour_text, font=font, fill=hour_outline_color)

    # Draw the hour text in white
    hour_text_color = "black"
    draw.text((hour_x, hour_y), hour_text, font=font, fill=hour_text_color)

    # Draw the minute text with a black border
    minute_outline_color = "black"
    minute_border_size = 2
    for i in range(-minute_border_size, minute_border_size + 1):
        for j in range(-minute_border_size, minute_border_size + 1):
            draw.text((minute_x + i, minute_y + j), minute_text, font=font, fill=minute_outline_color)

    # Draw the minute text in white
    minute_text_color = "black"
    draw.text((minute_x, minute_y), minute_text, font=font, fill=minute_text_color)

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
