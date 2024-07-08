#!/usr/bin/python
import secrets

# Ideally should generate random 14 character password
pass_len = 14
print(secrets.token_urlsafe(pass_len))