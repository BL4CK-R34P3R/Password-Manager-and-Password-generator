#!/usr/bin/env bash
File=encoded.txt
if test -f "$File"; then
	echo "data decoded ready to use"
	data=`cat encoded.txt`
	decoded=`echo "$data" | base64 -d`
	echo "$decoded" > password.txt
else 
	echo "Nothing to decode"
fi