#!/bin/bash

# Set the file path to the image directory
image_dir="/mnt/us/mayclock/anteaters"

# Function to stop the script gracefully
stop_script() {
    echo "Stopping the script..."
    exit 0
}

# Trap the SIGINT signal (Ctrl+C) to stop the script gracefully
trap stop_script SIGINT

# Function to get the adjusted hour based on the offset
get_adjusted_hour() {
    current_hour=$(date +"%H")
    adjusted_hour=$((current_hour + $1))
    
    # Handle wrapping around midnight
    if (( adjusted_hour < 0 )); then
        adjusted_hour=$((adjusted_hour + 24))
    elif (( adjusted_hour >= 24 )); then
        adjusted_hour=$((adjusted_hour - 24))
    fi
    
    printf "%02d" $adjusted_hour
}

# Main script loop
while true; do
    # Get the current time in the format HHMM
    current_time=$(date +"%M")

    # Get the adjusted hour based on the offset
    hour_offset=1  # Specify the hour offset, e.g., -1 for 1 hour behind, +1 for 1 hour ahead
    adjusted_hour=$(get_adjusted_hour $hour_offset)

    # Generate the filename based on the adjusted hour and current minute
    filename="${adjusted_hour}${current_time}.jpg"

    # Construct the full path to the image
    image_path="${image_dir}/${filename}"

    # Display the current time on the Kindle screen
    eips -g "$image_path"

    # Wait for 1 minute before the next iteration
    sleep 60
done
