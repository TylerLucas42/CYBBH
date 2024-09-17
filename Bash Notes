

General Stuff:
Add "2>/dev/null" to the end of any command to eliminate error messages from output (sends them to null)
Braces {} allow you to execute a command multiple times with different arguments, ie.
    example: "mkdir directory/{subdir1,subdir2,subdir3}" (creates directory, directory/subdir1, directory/subdir2, and directory/subdir3)

Find arguments:
    -exec
        "find /var/log/ -iname *.log -exec ls -al {} 2>/dev/null \;" (finds all .log files within /var/log then executes ls -al for each result from the find command)
        To instead execute ls -al for all results all at once and only once, replace "\;" with "+"
    Timestamp-based
        -atime 3 = accessed in last 3 days
        -amin -60 = accessed in last hour
        -ctime X = changed in last X days
        -cmin -X = changed in last X mins
        -mtime X = modified in last X days
        -mmin -X = modified in last X mins
    -iname *.txt (finds all files ending in .txt, not case sensitive)
