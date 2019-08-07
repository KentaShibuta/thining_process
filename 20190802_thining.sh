#!/bin/sh
echo ファイルのパスを入力:
read file_name
#echo 何行ごとにとりだす:
#read line_num 
#awk '{if(($2!~"nan")&&(NR%10==1)){printf "%e %e %e %e %e \n", $1, $2, $3, $4, $5 > "test.txt"}}' $file_name
awk '{if(($2!~"nan")&&(NR%1000==1)){print $1, $2, $3, $4, $5 > "test.txt"}}' $file_name

