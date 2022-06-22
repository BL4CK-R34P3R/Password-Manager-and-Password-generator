#!/usr/bin/env bash
File=password.txt
if test -f "$File"; then
	echo "data encoded"
	data=`cat password.txt`
	encoded=`echo "$data" | base64`
	echo "$encoded" > encoded.txt
  cp encoded.txt .enc
	rm password.txt
else
	echo "Nothing to encode"
fi
