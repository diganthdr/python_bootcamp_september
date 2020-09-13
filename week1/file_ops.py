
fd = open("readme.txt", "a+")
fd.write("Try to write more... ")
print(fd.readlines())

#fd, read, write, append