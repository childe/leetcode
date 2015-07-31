#!/usr/bin/env bash

# osx
grep -E "^(\d{3}-)|(\(\d{3}\) )\d{3}-\d{4}" file.txt

# linux
grep -P "^((\d{3}-)|(\(\d{3}\) ))\d{3}-\d{4}$" file.txt
