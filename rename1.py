import os
import glob


path = r"C:\Users\IsmartSiva\Downloads\signlanguagehema\\"
# search text files starting with the word "sales"
pattern = path + "i1\\"+ "*.jpg"

# List of the files that match the pattern
result = glob.glob(pattern)

# Iterating the list with the count
count = 43
for file_name in result:
    old_name = file_name
    new_name = path +"i1\\" + str(count) + ".jpg"
    os.rename(old_name, new_name)
    print("fgvd")
    count = count + 1

# Renaming the file
os.rename(old_name, new_name)