#!/bin/bash 
FOO=123
test() {
    FOO=321
}

echo “${FOO}”
test
echo “${FOO}”
exit 0
