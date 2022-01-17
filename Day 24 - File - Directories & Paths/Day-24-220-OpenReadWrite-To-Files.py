# By default the mode of files are "mode=r" read
# If a file does not exist it'll create it
# This is how to open the file and then close it
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# This method opens the file and closes it with out saying close
with open("my_file.txt") as file1:
    contents1 = file1.read()
    print(contents1)

# Writing to the files
with open("my_file.txt", mode='a') as file2:
    file2.write("\nNew text.")




