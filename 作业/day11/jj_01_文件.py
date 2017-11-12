file = open("english",encoding="utf8")
file2 = open("English1","w",encoding="utf8")

while True:
    text = file.readline()
    if not text:
        break
    file2.write(text)

file.close()
file2.close()