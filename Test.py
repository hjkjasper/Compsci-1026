# TODO: type solution here
text = open("text.txt","r")
myfile=open("myfile.txt","w")
for line in text :
    line = line.split()
    for word in line :
        word = word.rstrip(".,?!")

myfile.write(word)
text.close()
myfile.close()
#add your code here