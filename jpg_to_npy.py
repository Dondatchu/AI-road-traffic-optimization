import os
import cv2
import numpy as np
from PIL import Image

# Define input image path (Modify this to your actual image path)
image_path = r"C:\Users\mohan\Downloads\rush-hour-traffic-jam-on-the-freeway.jpg"

# Define output directory
save_dir = r"D:\Real time road optimization\Real time road optimization\Real time road optimization\inputs"
os.makedirs(save_dir, exist_ok=True)  # Ensure the directory exists

# Function to generate a unique filename if the file already exists
def get_unique_filename(directory, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}({counter}){ext}"
        counter += 1
        
    return os.path.join(directory, new_filename)

# Generate a unique .npy filename
npy_save_path = get_unique_filename(save_dir, "image.npy")

# Check if the input file exists
if not os.path.exists(image_path):
    print(f"Error: File '{image_path}' not found! Check the path.")
    exit()

# Try reading the image with OpenCV
image = cv2.imread(image_path)

if image is None:
    print("Error: OpenCV couldn't read the image. Trying with PIL...")

    try:
        # Try loading with PIL (in case OpenCV fails)
        image = Image.open(image_path).convert("RGB")

        # Convert to NumPy array
        image = np.array(image)

        # Save a fixed image in case of issues
        fixed_path = os.path.join(save_dir, "fixed_image.jpg")
        Image.fromarray(image).save(fixed_path)
        print(f"Fixed image saved as '{fixed_path}', try using this instead.")

    except Exception as e:
        print("Error: Unable to open image with PIL.", e)
        exit()

# Save the image as .npy in the unique path
np.save(npy_save_path, image)
print(f"Image successfully saved as '{npy_save_path}'")

