from sys import argv;import string
#chars=string.ascii_letters+string.digits
try:
	chars="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	def gtkey(key, plaintxt, keyd="", counter=0):
		while len(keyd) != len(plaintxt):
			if counter == len(key): counter = 0
			if plaintxt[len(keyd)] == " ": keyd += " "
			keyd += key[counter]
			counter += 1
		return keyd
	do=lambda a,op,b:a+b if op=="+" else a-b
	def endecrypt(string, key="",action="encrypt"):
		key,chi= gtkey(key, string),""
		for i in range(len(string)):
			if string[i] in chars:chi+=chars[do(chars.index(string[i]),"+" if action=="encrypt" else "-",chars.index(key[i]))%len(chars)]
			else:chi+=string[i]
		return chi
	print(endecrypt(argv[2],argv[3],argv[1]))

	"""
	def writer(path,key,action,enfile=""):
		filecopy=[i for i in open(path)]
		for i in filecopy:enfile+=endecrypt(i,key,action)
		open(path,"w").write(enfile)
	try:action,key,path=argv[1],argv[2],argv[3];writer(r""+path,key,action)
	"""
except:
	print("Vigenère_cipher Tool")
	print("%s [action:(encrypt->Defult Action,decrypt)] [Key] [File path] "%(argv[0].split("\\")[-1]))
	print("EX:\n\t%s encrypt \"mat12\" \"D:/myfile.txt\" "%(argv[0].split("\\")[-1]))
