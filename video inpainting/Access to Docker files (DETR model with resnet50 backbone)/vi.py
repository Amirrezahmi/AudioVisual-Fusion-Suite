"""vi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qk_ybtHAqAU1CxZhmbxRmS-zbi4Uy_6y
"""

#!pip install transformers

#!pip install timm

import os
import cv2
from PIL import Image
import numpy as np
from transformers import pipeline
import ffmpegcv

def video_to_frames(video_path, frames_dir):
    video = ffmpegcv.VideoCapture(video_path)
    count = 0
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        cv2.imwrite(frames_dir + "/{:d}.png".format(count), frame)
        count += 1
    video.release()
    # cv2.destroyAllWindows()
    return count




# video1_path = os.getenv('VIDEO1_PATH')
# video2_path = os.getenv('VIDEO2_PATH')


cwd = os.getcwd()


folder = 'videos'

# video1.mp4 and video2.mp4
video1_path = os.path.join(cwd, folder, 'video1.mp4')
video2_path = os.path.join(cwd, folder, 'video2.mp4')


# os.makedirs('file15', exist_ok=True)
# os.makedirs('file16', exist_ok=True)


# frames_count_1 = video_to_frames(video1_path, 'file15')
# frames_count_2 = video_to_frames(video2_path, 'file16')



os.makedirs('/opt/app/file15', exist_ok=True)
os.makedirs('/opt/app/file16', exist_ok=True)
aa='/opt/app/file15'
bb='/opt/app/file16'


frames_count_1 = video_to_frames(video1_path, aa)
frames_count_2 = video_to_frames(video2_path, bb)



# frames_count_1 = video_to_frames(video1_path, '/home/amirreza/Desktop/vi/file15')
# frames_count_2 = video_to_frames(video2_path, '/home/amirreza/Desktop/vi/file16')

#assert frames_count_1 == frames_count_2, "The number of frames in the two videos are not equal."

import shutil

# Define the directories
dir1 = aa
dir2 = bb

# Get the list of all files in directory 1
files_dir1 = set(os.listdir(dir1))

# Get the list of all files in directory 2
files_dir2 = set(os.listdir(dir2))

# Find the files which are in directory 2 but not in directory 1
files_to_delete = files_dir2 - files_dir1

# Remove these files from directory 2
for file in files_to_delete:
    file_path = os.path.join(dir2, file)
    if os.path.isfile(file_path):
        os.remove(file_path)



# Define the directories
dir2 = aa
dir1 = bb

# Get the list of all files in directory 1
files_dir1 = set(os.listdir(dir1))

# Get the list of all files in directory 2
files_dir2 = set(os.listdir(dir2))

# Find the files which are in directory 2 but not in directory 1
files_to_delete = files_dir2 - files_dir1

# Remove these files from directory 2
for file in files_to_delete:
    file_path = os.path.join(dir2, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

import os

# Specify the folder where your images are located
folder_path = aa

# List all files in the folder
files = os.listdir(folder_path)

# Sort the files by their numerical names
sorted_files = sorted(files, key=lambda x: int(x.split('.')[0]))

# Now, sorted_files contains your image filenames in numerical order
#print(sorted_files)
print("Great...")



# import numpy as np
# from PIL import Image
# from transformers import pipeline

# Load the model for image segmentation





model = pipeline("image-segmentation", device=0) 




# Directory containing frames of the first video
frame1_dir = aa

# Directory containing frames of the second video
frame2_dir = bb

# Directory to save the output frames
output_dir = 'output_frames33'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Get the list of frame files
frame_files1 = sorted_files
frame_files2 = sorted_files

# Ensure the number of frames in both videos are the same
assert len(frame_files1) == len(frame_files2), "The number of frames in both videos must be the same."

# Get the labels to keep from the first frame... actually 20
results = model(os.path.join(frame1_dir, frame_files1[20]))
for i, result in enumerate(results):
    print(f"{i}: {result['label']}")
labels_input = input("Enter the labels to keep, separated by space: ")
labels = labels_input.split()

# Loop over each pair of frames
for frame_file1, frame_file2 in zip(frame_files1, frame_files2):
    # Load the frames
    frame1 = Image.open(os.path.join(frame1_dir, frame_file1))
    frame2 = Image.open(os.path.join(frame2_dir, frame_file2))

    # Ensure both frames have the same size
    if frame1.size != frame2.size:
        frame1 = frame1.resize(frame2.size)

    # Segment the first frame
    results = model(frame1)

    # Create a dictionary mapping labels to masks
    label_to_mask = {result['label']: result['mask'] for result in results}

    # Initialize a binary mask with all zeros
    combined_binary_mask = np.zeros_like(np.array(results[0]["mask"]))

    for label in labels:
        # Check if the label is in the results
        if label not in label_to_mask:
            continue

        # Convert the mask to a numpy array
        mask_array = np.array(label_to_mask[label])

        # Apply a threshold to convert the grayscale mask to binary
        threshold = 128  # Adjust this threshold value as needed
        binary_mask = np.where(mask_array >= threshold, 255, 0).astype(np.uint8)

        # Combine the binary masks using the logical OR operation
        combined_binary_mask = np.logical_or(combined_binary_mask, binary_mask)

    # Convert the combined binary mask to uint8
    combined_binary_mask = combined_binary_mask.astype(np.uint8) * 255

    # Create a transparent image
    transparent_image = Image.new("RGBA", frame1.size, (0, 0, 0, 0))

    # Paste the original image onto the transparent image using the combined binary mask
    transparent_image.paste(frame1, (0, 0), mask=Image.fromarray(combined_binary_mask))

    # Overlay the transparent image onto the second frame
    frame2.paste(transparent_image, (0, 0), transparent_image)

    # Save the output frame
    frame2.save(os.path.join(output_dir, frame_file2))

# Combine the output frames back into a video
frame_files = sorted_files

frame0 = cv2.imread(os.path.join(output_dir, frame_files[0]))
height, width, layers = frame0.shape

# Use ffmpegcv.VideoWriter instead of cv2.VideoWriter
video = ffmpegcv.VideoWriter('/opt/app/videos/output_video.mp4', None, 26, (width, height))

for frame_file in frame_files:
    video.write(cv2.imread(os.path.join(output_dir, frame_file)))

video.release()