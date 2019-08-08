#!/bin/sh
echo ファイルのパスを入力:
read input_file_name
output_file_name=`date +"%Y%m%d%H%M%S"`
#awk '{if(($2!~"nan")&&(NR%10==1)){printf "%e %e %e %e %e \n", $1, $2, $3, $4, $5 > "test.txt"}}' $file_name
echo $output_file_name
awk 'BEGIN{
		OFS = ","
	}
	{if(($2!~"nan")&&(NR%1000==1))
		{print $1, $2, $3, $4, $5>"'"${output_file_name}"'.csv"}
	}' $input_file_name
