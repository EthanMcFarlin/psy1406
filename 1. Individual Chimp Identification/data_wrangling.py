import os
import shutil

# Create the new directory for the renamed images
if not os.path.exists('renamed_images'):
    os.makedirs('renamed_images')

# Initialize counters for Fredy and non-Fredy images
fredy_counter = 0
non_fredy_counter = 0

# Open the annotations file
with open('annotations_ctai.txt', 'r') as f:
    lines = f.read().split('Filename ')
    for line in lines[1:]:
        # Split the line into its components
        components = line.split()
        # Get the original filename and the name attribute
        original_filename = components[0].split('/')[-1]
        name_attribute = components[2]

        # Check if the name attribute is 'Fredy' and if we haven't already processed 50 'Fredy' images
        if name_attribute == 'Fredy' and fredy_counter < 50:
            # Create the new filename
            new_filename = original_filename.replace('.png', '_Positive_Fredy.png')
            # Increment the 'Fredy' counter
            fredy_counter += 1
        # Check if the name attribute is not 'Fredy' and if we haven't already processed 50 non-'Fredy' images
        elif name_attribute != 'Fredy' and non_fredy_counter < 50:
            # Create the new filename
            new_filename = original_filename.replace('.png', '_Negative.png')
            # Increment the non-'Fredy' counter
            non_fredy_counter += 1
        else:
            # If neither of the above conditions are met, continue to the next line
            continue

        # Rename the file and move it to the new directory
        shutil.copy(os.path.join('face_images', original_filename), os.path.join('renamed_images', new_filename))