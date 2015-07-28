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
    #awk -v i=$((1+index)) '{ if(1==NR){printf "%s",$i} else{printf " %s",$i} }END{printf "\n"}' file.txt
    #awk -v i=$((1+index))  '{if (NR==1) space=""; else space=" "} {printf "%s%s",space,$i} END {printf "\n"}' file.txt
    #awk '{if (NR==1) space=""; else space=" "} {printf "%s%s",space,$'$((1+index))'} END {printf "\n"}' file.txt
    cut -f $((1+index)) -d" " file.txt |tr "\n" " "
    echo
done
