#!/usr/bin/env bash
awk '
    {
    for (i=1; i<=NF; i++){
        s[NR,i] = $i;
    }
    f=NF
    }

    END{
    for (i=1;i<=f;i++){
        for(j=1;j<NR;j++){
            printf("%s ",s[j,i])
        }
        printf("%s\n",s[j,i])
    }
    }
' file.txt
