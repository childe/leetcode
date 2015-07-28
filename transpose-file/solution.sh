#!/usr/bin/env bash
#columncount=$(head -n1 file.txt|awk '{print NF}')
#echo $columncount
#for i in {1..$((columncount+0))}
#do
    #echo $i
#done


read -a array <<< $(head -n1 file.txt)
#wc=$(wc -l file.txt)
for index in "${!array[@]}"
do
    #echo "$index ${array[index]}"
    #awk -v i=$((1+index))  -v wc=$((0+wc)) '{if (NR==wc) space="\n"; else space=" "} {printf "%s%s",$i,space}' file.txt
    awk -v i=$((1+index)) '{printf "%s ",$i}' file.txt | sed 's/^[[:space:]]*//'
done
