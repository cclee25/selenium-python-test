with open("text.txt", "r") as source_file:
    content = source_file.readlines()

with open("output_file.txt", "w") as output_file:
    for line in sorted(content, reverse=True):
        output_file.write(line)

with open("text.txt", "r") as source_file1:
    content1 = source_file1.readline()

with open("output_file1.txt", "w") as output_file1:
    for char in sorted(content1, reverse=True):
        output_file1.write(char)

with open("text.txt", "r") as source_file2:
    content2 = source_file2.readlines()

with open("output_file2.txt", "w") as output_file2:
    for line1 in reversed(content2):
        output_file2.write(line1)