#!/bin/bash

sudo su

today=`(date +%d-%m-%Y_%H:%M:%S)`

dir=${fname}
default=${default}
seqno=${seqno}
cd $default/$seqno

sudo cp /home/alamy/s3upload.py .
echo "Starting the Upload "

for files in "$dir"*.tar.gz;
 do
 	/usr/bin/python s3upload.py ${bucketname} $files
 	sudo echo "uploaded tar file "$files "at" $today >> $dir"/script.log"
 done

echo " "
sudo echo "upload of tar files for sequence completed "$dir "at" $today >> $dir"/script.log"
echo "uploading of tar files to s3 completed... Thanks"

mail -s "tar uploading to s3 completed for "$dir -A $dir"/script.log" itsdprojectalerts@alamy.com


