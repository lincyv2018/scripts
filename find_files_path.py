
import os
import glob
fulllist = "listoffile.log"
sorece = open(fulllist, "r")
output = open("tobedeleted.log", "a+")
for line1 in sorece:
    sword = line1.split('/')
#    print sword
    temp = sword[1].split(".")
    for filename in glob.glob('*.csv'):
        f = open(filename, "r")
        for line in f:
            word = line.split(',')
            filename = word[0]
            if temp[0] == filename:
               print word[0], word[2]
               data = word[0]+","+word[2]
               output.write(data)
output.close()
print "Process Completd"
