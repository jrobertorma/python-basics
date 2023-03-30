#!/bin/bash
> oldFiles.txt
files=$(grep ' jane ' ~/data/list.txt | cut -d ' ' -f 3)
for file in $files; do
        if test -e "~${file}"; then
                echo "File exists";
                >> oldFiles.txt;
        else
                echo "File doesn't exist";
        fi
done

# Take care of the frikin' curly braces when calling a variable as an argument of a command (see line 5) >:(