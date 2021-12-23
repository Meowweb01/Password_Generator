import string
import random

def main():
	s1 = string.ascii_uppercase
	s2 = string.ascii_lowercase
	s3 = string.digits
	s4 = string.punctuation

	pass_len = int(input("Please enter your password length: "))
	
	s = []
	s.extend(list(s1))
	s.extend(list(s2))
	s.extend(list(s3))
	s.extend(list(s4))


	for a in range(1024):
		random.shuffle(s)

	print("".join(s[0:pass_len]))


if __name__ == "__main__":
	main()