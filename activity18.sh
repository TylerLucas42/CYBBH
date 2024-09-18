#!/bin/bash

mkdir ~/ZIP
echo -n 12345 | md5sum | sed 's/  -//g' > ~/ZIP/file1
echo -n 6789 | md5sum | sed 's/  -//g' > ~/ZIP/file2
echo -n abcdef | md5sum | sed 's/  -//g' > ~/ZIP/file3
zip -r -j ~/ZIP/file.zip ~/ZIP/*
tar -czf ~/ZIP/file.tar.gz ~/ZIP/file.zip
