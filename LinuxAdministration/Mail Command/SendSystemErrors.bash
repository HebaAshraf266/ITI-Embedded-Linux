#!/bin/bash 

grep -r power /sys/ 2> /dev/null >ErrorFile

mail -s "ErrorFile" -A ErrorFile hebaashraf26699@gmail.com
