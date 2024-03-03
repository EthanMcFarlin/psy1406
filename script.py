import os
from collections import Counter

# Step 1: Create a mapping of filenames to gender attributes from the annotations file
filename_to_gender = {}
with open('annotations_ctai.txt', 'r') as annotations_file:
    for line in annotations_file:
        if line.startswith("Filename"):
            parts = line.strip().split()
            filename_index = parts.index("Filename") + 1
            gender_index = parts.index("Gender") + 1
            filename = parts[filename_index]
            gender = parts[gender_index]
            filename_to_gender[filename] = gender

# Step 2: Define the source and target directories
face_images_dir = 'face_images'
renamed_images_dir = 'renamed_chimp_images'

# Create the target directory if it doesn't exist
if not os.path.exists(renamed_images_dir):
    os.makedirs(renamed_images_dir)

# Step 3: Initialize counters for male and female images
gender_counters = Counter()

# Step 4: Iterate over the files in the 'face_images' directory and rename them
for filename in os.listdir(face_images_dir):
    if filename.endswith('.png'):
        full_path = os.path.join(face_images_dir, filename)
        gender = filename_to_gender.get(full_path)
        
        # Check if the gender count for this gender has not yet reached 125
        if gender and gender_counters[gender] < 125:
            new_name = filename
            if gender.lower() == 'male':
                new_name = filename.replace('.png', '_Positive_Male.png')
            elif gender.lower() == 'female':
                new_name = filename.replace('.png', '_Negative_Female.png')
            
            # Step 5: Move the renamed file to the new directory
            new_path = os.path.join(renamed_images_dir, new_name)
            os.rename(full_path, new_path)
            
            # Increment the counter for the gender
            gender_counters[gender] += 1
            
            # Check if we have reached 125 for both genders
            if all(count >= 125 for count in gender_counters.values()):
                break
        else:
            # Skip the file if the gender count has been reached or if no gender is found
            continue

print("Renaming and moving complete.")
print(f"Moved {gender_counters['Male']} male and {gender_counters['Female']} female images.")