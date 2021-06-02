"""
Read file
Write to file
"""

print("== open file read==")
with open('temp.txt', 'r', encoding='utf-8') as fp:  # fp is the stream object

    print(f"reading file name: {fp.name}, encoding: {fp.encoding}, mode: {fp.mode}")
    
    print(fp.read())
    print(f"location in file: {fp.tell()}")
    
    fp.seek(0)  # move to 0th byte
    print(f"location in file after seek to 0: {fp.tell()}")

    print(f"next character: {fp.read(1)}") # read 1 character (if open uses 'rb' mode i.e. binary file, this would be reading 1 byte)

    for line in fp:
        print(f"{line.rstrip():>4}")     
print()

print("== open file write ==")
with open('temp1.txt', 'w', encoding='utf-8') as fp:  # fp is the stream object
    print(f"writing file name: {fp.name}, encoding: {fp.encoding}, mode: {fp.mode}")    
    fp.write('test line 1\n')
    fp.write('test line 2\n')
with open('temp1.txt', 'r', encoding='utf-8') as fp:  # fp is the stream object
    print(f"reading file name: {fp.name}, encoding: {fp.encoding}, mode: {fp.mode}")
    for line in fp:
        print(f"{line.rstrip():>4}")     
print()
