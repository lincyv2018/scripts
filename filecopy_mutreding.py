import threading
import multiprocessing
import sys
import os
import tarfile
import glob
import datetime
import smtplib
from shutil import copy

#from shutil import copyfile
sucess_log_path = "/mnt/highrestos3/Logs/Success/SnowBall"
fail_log_path = "/mnt/highrestos3/Logs/Failed/SnowBall"

logname = sys.argv[1] #"photos003_1003846-003_1003870.csv"
destnametion =  sys.argv[2]#"./photos003_1003846-003_1003870"
SERVER = "localhost"
FROM = "noreply@alamy.com"
TO = ["itsdprojectalerts@alamy.com"] # must be a list
SUBJECT = "HiRes Snowball Job Status for "+logname
TEXT = "HighRes Snowball getfile process completed"+str(datetime.datetime.now())

if sys.argv[1] == " " or  sys.argv[2] == " ":
    print "argument are missing"
    quit()
comfile = logname.split(".")
archive_name = comfile[0]+".tar.gz"
sucess_log = open(logname+"-sucess.log", "a+")
fail_log = open(logname+"-fail.log", "a+")
process_log = open(logname+".log", "a+")
def okay():
    print("Done.\n")
process_log.write("process started"+str(datetime.datetime.now()))
with open(logname) as f:
    for line in f:
        word = line.split(',')
        filename = word[2].split("\\")
        print word[2]
        print filename[6]
        ext = filename[6].split('.')
        print ext[1]
        newname = word[0]+"."+ext[1].rstrip()
        print newname
        try:
            threading.Thread(copy(word[1], destnametion+"/"+newname)).start()
            sucess_log.write(word[2])
        except:
            fail_log.write(word[2])
            print word[1]+" file not found"
            pass
process_log.write("compression started"+str(datetime.datetime.now()))
print("Compressing files to %s..." % archive_name)
tar = tarfile.open(archive_name, "w:gz")
for file_name in glob.glob(os.path.join(destnametion, "*")):
    print("  Adding %s..." % file_name)
    multiprocessing.Process(tar.add(file_name, os.path.basename(file_name))).start()
tar.close()
okay()

process_log.write("Process ended"+str(datetime.datetime.now()))
sucess_log.close()
fail_log.close()
process_log.close()
copy(logname+"-sucess.log",sucess_log_path)
copy(logname+"-fail.log",fail_log_path)
##### email process
TEXT = "HighRes Snowball getfile process completed"+str(datetime.datetime.now())
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()
threading.exit()
