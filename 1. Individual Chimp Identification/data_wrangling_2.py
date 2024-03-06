import os

# Define the anchor image
anchor_image = 'img-id54-object-1_Anchor_Fredy.png'

# Initialize the list of image pairs
image_pairs = []

# Get the list of all files in the 'renamed_images' directory
all_files = os.listdir('renamed_images')

# Loop through all the files
for file in all_files:
    # Skip the anchor image
    if file == anchor_image:
        continue
    # Add the pair to the list
    image_pairs.append((anchor_image, file))

# Print the list of image pairs
for pair in image_pairs:
    print(pair)