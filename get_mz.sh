#!/bin/bash
hosts=$(httpd -S)
content=$(curl -L www.mz.com)
echo $content
