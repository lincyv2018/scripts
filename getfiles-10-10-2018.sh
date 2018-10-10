#!/bin/bash
sudo su
# folder name with full path 
dir=${filename}
# default store dir
default=${default}
# secuence number 

seqno=${seqno}

cd $default/$seqno

sout=${sout}
fout=${fout}

today=`(date +%d-%m-%Y_%H:%M:%S)`

sudo echo "checking available of mount" $today >> $dir"/script.log"
if [ ! -d "/smb/" ]; then
 sudo echo "mount unavailable. script terminated" $today >> $dir"/script.log"
 echo "script terminates as mount unavailable... Thanks" | mail -s "mount unavailable for copy "$dir -A $dir"/script.log" itsdprojectalerts@alamy.com
 exit
fi;

echo "image copy and compression started for "$dir "at" $today >> $dir"/script.log"
echo " "
for files in "$dir"/*.csv;
do

 fn=$(basename $files .csv)
 infile="$dir"/$fn.csv

 echo "creating directory "$fn" to copy file" >> $dir"/script.log"
 if [ -d "$dir"/$fn ]; then
  echo "directory "$fn" already exists" >> $dir"/script.log"
  echo "script terminates as directory already exisits... Thanks" | mail -s "directory exisits confirm rerun "$dir -A $dir"/script.log" itsdprojectalerts@alamy.com
  exit
 else
  sudo mkdir "$dir"/$fn
 fi;

 sudo echo "reading csv file "$fn".csv" >> $dir"/script.log"
 sudo echo "copy images started for file "$fn".csv at" $today >> $dir"/script.log"

 IFS=,
 while read -r c1 c2 c3
 do

  if [ -f $c2 ]; then
   sudo cp $c2 "$dir"/$fn/$c1.${c2##*.}; echo "${c3}" &>> $dir/$fn"_success.log"
  else
   sudo echo "${c3}" &>> $dir/$fn"_failed.log"
  fi;

 done < $infile

 sudo echo "copy images completed for file "$fn".csv at" $today >> $dir"/script.log"

 echo "compression started for folder "$fn "at" $today >> $dir"/script.log"
 sudo tar -cvzf "$dir"/$fn.tar.gz --absolute-names $dir/$fn &
 echo "compression completed for folder "$fn "at" $today >> $dir"/script.log"
 echo " "
 echo " copying the log $fn "
sudo cp $dir/$fn"_success.log" $sout/$seqno && cp $dir/$fn"_failed.log" $fout/$seqno

done


echo " "
echo "image copy and compression completed for "$dir "at" $today >> $dir"/script.log"
echo " "

echo "printing success and failed count for "$dir "at" $today >> $dir"/script.log"
echo " "
echo "success count" $today >> $dir"/script.log"
for files in "$dir"/*_success.log;
 do
 wc -l $files >> $dir"/script.log"
 done
echo " "
echo "failed count" $today >> $dir"/script.log"
for files in "$dir"/*_failed.log;
 do
 wc -l $files >> $dir"/script.log"
 done
echo " "
echo "printing size information of "$dir "at" $today >> $dir"/script.log"
du -sh "$dir"/* >> $dir"/script.log"
echo " "
echo "Copy and compression of images completed... Thanks" | mail -s "Copy and Compress completed for "$dir -A $dir"/script.log" itsdprojectalerts@alamy.com
