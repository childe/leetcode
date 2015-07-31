awk '
{
    for(i=1;i<=NF;i++){
        s[$i]+=1
    }
}
END{
    for (word in s){
        print word, s[word]
    }
}
' words.txt |sort -rnk2
