#!/bin/bash
#vmcmd=$(httpd -S)
hosts='/Users/kbeattie/Desktop/hosts'
zone='www.mz.com'

function getWebPage {
  echo Curling web page for $zone
  curl -L $zone
}

if grep -q "$zone" $hosts; then
  echo Found $zone in Apache VM hosts
  getWebPage $zone
else
  echo Did not find $zone in Apache VM hosts
fi
#content=$(curl -L www.mz.com)
#echo $content
