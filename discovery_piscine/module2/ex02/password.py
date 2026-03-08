#!/usr/bin/env python3

# Şifreyi tanımlıyoruz
secret_password = "Python is awesome"

try:
	#kullaıcıdan giriş alıyoruz 
	user_input = input()
	#kontrol saglıyoruz
	if user_input == secret_password:
		print("access granted")
	else:
		print("access denied")
except EOFError:
	pass
