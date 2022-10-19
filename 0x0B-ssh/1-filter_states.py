#!/usr/bin/env bash
# Bash script that creates an RSA key pair
#ssh-keygen -b 4096 -P betty -f school
ssh-keygen -t rsa -b 3072 -P betty -f school
