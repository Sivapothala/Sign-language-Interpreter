import glob
import os
from PIL import Image

path = r"C:\Users\IsmartSiva\Downloads\Sravani_Signs\\"
# search text files starting with the word "sales"
pattern = path + "Language\\"+ "*.jpeg"

# List of the files that match the pattern
result = glob.glob(pattern)
# print(result)
# Iterating the list with the count
count = 138
for file_name in result:
    print("dfd")
    image = Image.open(file_name)
    new_image = image.resize((300, 360))
    new_image.save('{}{}{}.jpg'.format(path,"Language1\\",str(count)))
    count = count + 1



