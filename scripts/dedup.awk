#!/usr/bin/awk -f

{
    if (!($1 in lines) || ($2 == "ca"))
        lines[$1] = $0
}

END{
    for (i in lines) 
        print lines[i]
}
