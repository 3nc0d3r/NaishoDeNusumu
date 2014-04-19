#!/bin/bash

# Create private key using 
openssl genrsa -out privkey.pem 12288
#openssl genrsa -out privkey.pem 17000

# Use private key to create public key
openssl rsa -in privkey.pem -pubout -out pubkey.pem
